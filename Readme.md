# 🌍 TripMate AI

*Give us your destination. We'll give you the plan.*

TripMateAI is a web application that generates personalized travel itineraries using Google's Gemini AI. Users can input their destination, travel dates, and interests to receive a detailed day-by-day plan.

## ✨ Features

- **AI-Powered Itineraries:** Generates comprehensive daily plans.
- **Hotel & Restaurant Suggestions:** Provides recommendations for accommodations and dining.
- **Personalized Activities:** Tailors activities based on user interests.
- **Integrated Google Maps:** Includes direct links to Google Maps for every location.
- **Simple Web Interface:** Built with Gradio for ease of use.

## 🚀 How to Run Locally

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/YOUR_USERNAME/TripMateAI.git
    cd TripMateAI
    ```

2.  **Set up a virtual environment:**
    ```bash
    python -m venv venv
    # On Windows: venv\Scripts\activate
    # On macOS/Linux: source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: You will need to create a `requirements.txt` file. See below.)*

4.  **Create a `.env` file:**
    Create a `.env` file in the root directory and add your Google AI API key:
    ```
    GOOGLE_API_KEY="YOUR_API_KEY_HERE"
    ```

5.  **Run the app:**
    ```bash
    python app.py
    ```
    Open the local URL (e.g., `http://127.0.0.1:7860`) in your browser.