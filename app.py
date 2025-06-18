from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import requests
import json
import os

app = Flask(__name__)
CORS(app)

OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "tinyllama"  # Back to llama2 with optimizations

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        
        if not data or 'message' not in data:
            return jsonify({
                'error': 'Please provide a message in the request body'
            }), 400
        
        user_message = data['message']
        
        try:
            ollama_payload = {
                "model": MODEL_NAME,
                "prompt": user_message,
                "stream": False,
                "options": {
                    "num_thread": 4,  # Limit CPU threads
                    "temperature": 0.7,  # More natural responses
                    "top_k": 40,  # More varied responses
                    "num_predict": 500  # Allow longer responses
                }
            }
            
            response = requests.post(OLLAMA_API_URL, json=ollama_payload)
            
            if response.status_code == 200:
                llm_response = response.json()
                bot_response = llm_response.get('response', 'Sorry, I could not generate a response.')
            else:
                bot_response = f"Error connecting to Ollama: {response.status_code}. Make sure Ollama is running with 'ollama serve'"
        
        except requests.exceptions.ConnectionError:
            bot_response = "Cannot connect to Ollama. Please ensure Ollama is installed and running with 'ollama serve'"
        except Exception as e:
            bot_response = f"Error with LLM: {str(e)}"
        
        return jsonify({
            'message': bot_response,
            'user_message': user_message,
            'status': 'success'
        })
    
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500

@app.route('/', methods=['GET'])
def home():
    # Serve the HTML file instead of JSON
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), 'test_chat.html')

@app.route('/api/info', methods=['GET'])
def api_info():
    return jsonify({
        'message': 'Welcome to the Chatbot API with Local LLM!',
        'endpoints': {
            '/chat': 'POST - Send a message to the chatbot'
        },
        'llm_info': {
            'model': MODEL_NAME,
            'backend': 'Ollama'
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)