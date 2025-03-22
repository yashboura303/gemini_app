# Gemini Chat Application

A web application that integrates Google's Gemini 1.5 Flash LLM with a Flask-based web UI.

## Features

- Clean, modern UI for chatting with Gemini
- Handles natural language queries
- Real-time streaming responses
- Mobile-responsive design

## Requirements

- Python 3.7+
- Flask
- Google GenerativeAI Python SDK

## Setup

1. Clone this repository
2. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Set up your Gemini API key in the `.env` file:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```
4. Run the application:
   ```
   python app.py
   ```
5. Open your browser and navigate to `http://127.0.0.1:5000`

## Usage

1. Type your question or prompt in the input field
2. Click "Send" or press Enter
3. Wait for Gemini to generate a response
4. Continue the conversation as desired

## Tech Stack

- Backend: Flask (Python)
- Frontend: HTML, CSS, JavaScript
- AI: Google Gemini 1.5 Flash

## License

MIT "# gemini_app" 
