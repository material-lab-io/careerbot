# Ollama Setup Instructions

## 1. Install Ollama

### For Linux/WSL:
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### For Windows:
Download from: https://ollama.com/download/windows

### For Mac:
Download from: https://ollama.com/download/mac

## 2. Start Ollama Service
```bash
ollama serve
```

## 3. Pull a Model (e.g., llama2)
```bash
ollama pull llama2
```

## 4. Available Models
- llama2 (7B parameters)
- mistral (7B parameters)
- codellama (for coding tasks)
- llama2:13b (larger model)
- llama2:70b (very large model)

## 5. Change Model in app.py
Edit line 10 in app.py to use a different model:
```python
MODEL_NAME = "mistral"  # or any other model
```

## 6. Test if Ollama is Running
```bash
curl http://localhost:11434/api/generate -d '{
  "model": "llama2",
  "prompt": "Hello"
}'
```

## Troubleshooting
- Make sure Ollama is running: `ollama serve`
- Check available models: `ollama list`
- Pull a model if needed: `ollama pull llama2`
- Default port is 11434