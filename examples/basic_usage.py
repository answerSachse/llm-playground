from src.models.openai_client import OpenAIClient

def main():
    # Initialize the client
    client = OpenAIClient()

    # Simple completion example
    prompt = "Explain what a large language model is in one sentence:"
    response = client.generate_completion(prompt)
    print("\nSimple Completion Example:")
    print(f"Prompt: {prompt}")
    print(f"Response: {response.choices[0].message.content}")

    # Chat completion example
    messages = [
        {"role": "system", "content": "You are a helpful AI assistant specializing in Python programming."},
        {"role": "user", "content": "What's the difference between a list and a tuple in Python?"}
    ]
    response = client.generate_chat_completion(messages)
    print("\nChat Completion Example:")
    print(f"System: {messages[0]['content']}")
    print(f"User: {messages[1]['content']}")
    print(f"Assistant: {response.choices[0].message.content}")

    # Token counting example
    text = "This is a sample text to count tokens from."
    token_count = client.count_tokens(text)
    print("\nToken Counting Example:")
    print(f"Text: {text}")
    print(f"Estimated token count: {token_count}")

if __name__ == "__main__":
    main()