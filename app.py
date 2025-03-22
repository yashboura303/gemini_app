from flask import Flask, render_template, request, jsonify
import requests
import os
import json
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Configure the app
app = Flask(__name__, static_folder='app/static', template_folder='app/templates')

# Add CORS headers to all responses
@app.after_request
def add_cors_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
    return response

# Handle OPTIONS requests for CORS preflight
@app.route('/chat', methods=['OPTIONS'])
def handle_options():
    return '', 204

# Simple test endpoint to check if the API is reachable
@app.route('/test', methods=['GET'])
def test():
    logger.debug("Test endpoint called")
    return jsonify({'status': 'ok', 'message': 'API is working'})

# Gemini API configuration
GEMINI_API_KEY = "AIzaSyAAP_LRVtyZe-X4t0cIN5JJMnfirfaOCiQ"
GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        logger.debug("Received chat request")
        
        # Print request data for debugging
        logger.debug(f"Request data: {request.data}")
        
        data = request.json
        logger.debug(f"Parsed JSON data: {data}")
        
        user_prompt = data.get('prompt', '')
        logger.debug(f"User prompt: {user_prompt}")
        
        if not user_prompt:
            logger.warning("No prompt provided")
            return jsonify({'error': 'No prompt provided'}), 400
        
        # Prepare request to Gemini API
        headers = {
            "Content-Type": "application/json",
        }
        
        payload = {
            "contents": [{
                "role": "user",
                "parts": [{"text": user_prompt}]
            }]
        }
        
        logger.debug(f"Sending request to Gemini API: {payload}")
        
        # Make request to Gemini API with API key in URL
        response = requests.post(
            f"{GEMINI_URL}?key={GEMINI_API_KEY}",
            headers=headers,
            json=payload
        )
        
        logger.debug(f"Gemini API response status: {response.status_code}")
        logger.debug(f"Gemini API response: {response.text}")
        
        # Parse response
        if response.status_code == 200:
            response_data = response.json()
            logger.debug(f"Parsed response data: {response_data}")
            # Extract text from response
            ai_response = response_data['candidates'][0]['content']['parts'][0]['text']
            logger.debug(f"AI response: {ai_response}")
            return jsonify({'response': ai_response})
        else:
            logger.error(f"API Error: {response.status_code} - {response.text}")
            return jsonify({'error': f"API Error: {response.status_code} - {response.text}"}), 500
    
    except Exception as e:
        logger.exception("Error in chat endpoint")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 