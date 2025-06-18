# CareerBot - AI Chat Assistant

An intelligent chat assistant powered by Ollama and Flask, featuring a modern web interface.

## Features

- 🤖 Local AI model integration using Ollama
- 💬 Real-time chat interface with typing indicators
- 🎨 Modern, responsive UI design
- 🚀 Fast response times with TinyLlama model
- 🔒 Privacy-focused - runs entirely locally

## Prerequisites

- Python 3.8+
- Ollama installed and running
- Node.js (for frontend assets)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/material-lab-io/careerbot.git
cd careerbot
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

4. Install and setup Ollama:
```bash
# Follow instructions in ollama_setup.md
ollama pull tinyllama
```

## Usage

1. Start Ollama service:
```bash
ollama serve
```

2. In a new terminal, run the Flask application:
```bash
python app.py
```

3. Open your browser and navigate to `http://localhost:5000`

## Project Structure

```
careerbot/
├── app.py              # Flask backend application
├── test_chat.html      # Frontend chat interface
├── requirements.txt    # Python dependencies
├── ollama_setup.md     # Ollama installation guide
└── README.md          # This file
```

## Configuration

The application uses TinyLlama by default for fast responses. You can change the model by modifying the `MODEL_NAME` variable in `app.py`.

## Development

To contribute to this project:

1. Create a feature branch
2. Make your changes
3. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.