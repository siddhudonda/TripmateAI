import os
import gradio as gr
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure the Google Generative AI client
try:
    genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
except AttributeError:
    print("Could not find GOOGLE_API_KEY. Make sure you have it set in a .env file.")
    exit()

def generate_trip_plan(from_loc, to_loc, start_date, end_date, interests):
    """
    Generates a trip plan using the Gemini LLM.
    """
    if not all([from_loc, to_loc, start_date, end_date]):
        return "## Please fill in all required fields: From, To, Start Date, and End Date."

    # --- This is the core of Prompt Engineering ---
    # We create a detailed prompt that tells the AI exactly what we want.
    # Using Markdown formatting in the prompt helps the AI structure the output.
    prompt = f"""
    You are TripMateAI, an expert travel planner. Create a detailed, day-by-day travel itinerary.
    Your response must be in Markdown format.

    **Travel Details:**
    - **Origin:** {from_loc}
    - **Destination:** {to_loc}
    - **Travel Dates:** {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}
    - **User Interests:** {interests if interests else 'General sightseeing, food, and culture.'}

    **Your Task:**
    Generate a complete travel plan that includes the following for each day:
    1.  **🏨 Suggested Hotels:** List 3 hotel recommendations (budget, mid-range, luxury) with a brief description. Do not make up websites, just provide names.
    2.  **🗺️ Day-by-Day Itinerary:** Provide a morning, afternoon, and evening plan for each day.
    3.  **🍴 Restaurant Recommendations:** Suggest 2-3 popular restaurants for lunch and dinner, mentioning the type of cuisine.
    4.  **🎯 Activities:** Tailor activities to the user's interests.
    5.  **📍 Google Maps Links:** For each location (hotel, restaurant, activity), provide a valid Google Maps search link in the format: `[Location Name](https://www.google.com/maps/search/?api=1&query=URL_ENCODED_LOCATION_NAME)`. For example, for the Eiffel Tower in Paris, the query would be `Eiffel+Tower+Paris`.

    Structure your entire response using Markdown with clear headings. Start with a summary of the trip.

    **Example Structure for a Day:**
    ---
    ### **Day 1: Arrival and Exploration**

    **Morning (9:00 AM - 12:00 PM):**
    - Arrive at [Airport/Station].
    - Check into your hotel.

    **Lunch (12:30 PM):**
    - **[Restaurant Name](https://www.google.com/maps/search/?api=1&query=...):** Brief description of the restaurant.

    **Afternoon (2:00 PM - 5:00 PM):**
    - **[Activity/Landmark Name](https://www.google.com/maps/search/?api=1&query=...):** Description of the activity.

    **Evening (7:00 PM onwards):**
    - **Dinner at [Restaurant Name](https://www.google.com/maps/search/?api=1&query=...):** Description.
    - **[Evening Activity](https://www.google.com/maps/search/?api=1&query=...):** Description.

    ---
    Now, generate the plan for the user's trip.
    """

    try:
        # Call the Gemini API
        response = model.generate_content(prompt)
        # Return the generated text, which is already in Markdown format
        return response.text
    except Exception as e:
        return f"An error occurred: {e}"

# --- Gradio Interface Definition ---
with gr.Blocks(theme=gr.themes.Soft(), title="TripMate AI") as demo:
    gr.Markdown(
        """
        # 🌍 TripMate AI
        *Give us your destination. We'll give you the plan.*
        """
    )

    with gr.Row():
        from_loc = gr.Textbox(label="From", placeholder="e.g., New York, USA")
        to_loc = gr.Textbox(label="To", placeholder="e.g., Paris, France")

    with gr.Row():
        start_date = gr.Date(label="Start Date")
        end_date = gr.Date(label="End Date")

    interests = gr.Textbox(label="Interests (Optional)", placeholder="e.g., nature, history, food, hiking")

    submit_btn = gr.Button("Generate Trip Plan", variant="primary")

    gr.Markdown("---")
    gr.Markdown("## Your AI-Generated Itinerary")

    # The output will be displayed here. `gr.Markdown` is perfect because our LLM returns Markdown.
    output_plan = gr.Markdown()

    submit_btn.click(
        fn=generate_trip_plan,
        inputs=[from_loc, to_loc, start_date, end_date, interests],
        outputs=output_plan
    )

# Launch the Gradio app
if __name__ == "__main__":
    demo.launch()