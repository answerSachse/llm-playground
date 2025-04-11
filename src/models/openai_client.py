import os
from typing import Dict, List, Optional, Union
from openai import OpenAI
from dotenv import load_dotenv

class OpenAIClient:
    """A client for interacting with OpenAI's API."""
    
    def __init__(self):
        """Initialize the OpenAI client with API credentials."""
        load_dotenv()
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.default_model = os.getenv("DEFAULT_MODEL", "gpt-4")
        self.max_tokens = int(os.getenv("MAX_TOKENS", "2000"))
        self.temperature = float(os.getenv("TEMPERATURE", "0.7"))

    def generate_completion(
        self,
        prompt: str,
        model: Optional[str] = None,
        max_tokens: Optional[int] = None,
        temperature: Optional[float] = None,
        **kwargs
    ) -> Dict:
        """Generate a completion for the given prompt.
        
        Args:
            prompt: The input text to generate completion for
            model: The model to use (defaults to environment setting)
            max_tokens: Maximum tokens in response (defaults to environment setting)
            temperature: Sampling temperature (defaults to environment setting)
            **kwargs: Additional parameters to pass to the API
        
        Returns:
            Dict containing the API response
        """
        response = self.client.chat.completions.create(
            model=model or self.default_model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens or self.max_tokens,
            temperature=temperature or self.temperature,
            **kwargs
        )
        return response

    def generate_chat_completion(
        self,
        messages: List[Dict[str, str]],
        model: Optional[str] = None,
        temperature: Optional[float] = None,
        **kwargs
    ) -> Dict:
        """Generate a chat completion for the given message history.
        
        Args:
            messages: List of message dictionaries with 'role' and 'content'
            model: The model to use (defaults to environment setting)
            temperature: Sampling temperature (defaults to environment setting)
            **kwargs: Additional parameters to pass to the API
        
        Returns:
            Dict containing the API response
        """
        response = self.client.chat.completions.create(
            model=model or self.default_model,
            messages=messages,
            temperature=temperature or self.temperature,
            **kwargs
        )
        return response

    def count_tokens(self, text: str) -> int:
        """Count the number of tokens in the given text.
        
        Args:
            text: The input text to count tokens for
        
        Returns:
            int: Number of tokens
        """
        # Note: This is a simplified implementation
        # For production use, consider using tiktoken
        return len(text.split()) * 1.3  # Rough estimate