# LLM Playground

A comprehensive playground for experimenting with Large Language Models (LLMs). This repository contains examples, utilities, and best practices for working with various LLM models and frameworks.

## Features

- 🤖 Model Integration Examples
  - OpenAI GPT Models
  - Hugging Face Transformers
  - Local LLM Deployment
- 🛠️ Utility Functions
  - Prompt Engineering Tools
  - Token Counting
  - Response Parsing
- 📊 Evaluation Tools
  - Model Performance Metrics
  - Response Quality Assessment
  - Cost Tracking
- 🔧 Best Practices
  - Prompt Engineering Guidelines
  - Error Handling
  - Rate Limiting
  - API Key Management

## Getting Started

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/answerSachse/llm-playground.git
cd llm-playground
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your API keys and configurations
```

## Project Structure

```
llm-playground/
├── examples/           # Example scripts and notebooks
├── src/               # Source code
│   ├── models/        # Model integrations
│   ├── utils/         # Utility functions
│   └── evaluation/    # Evaluation tools
├── tests/             # Test cases
├── configs/           # Configuration files
└── docs/             # Documentation
```

## Usage Examples

Check the `examples/` directory for various use cases and demonstrations.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- OpenAI for their GPT models
- Hugging Face for their Transformers library
- The LLM community for sharing knowledge and best practices