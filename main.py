import base64
import json
import logging
import os
import uuid
from io import BytesIO

import google.generativeai as genai
from PIL import Image

# Initialize the logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
logger.addHandler(handler)

# Initialize Google AI
genai.configure(api_key="TEIDÄN API-KEYNNE TÄHÄN")

# Make API endpoint for this function. Last project group used django for this. You can also use Flask or FastAPI.
# I suggest you to use FastAPI because it is faster than Flask and it is easy to use. https://fastapi.tiangolo.com/
def analyze_image(image_path):
    # Open the image file
    with Image.open(image_path) as img:
        # Convert the image to RGB mode if it's not already
        if img.mode != 'RGB':
            img = img.convert('RGB')

        # Resize the image if it's too large
        max_size = 3072
        if max(img.size) > max_size:
            img.thumbnail((max_size, max_size))

        # Convert the image to base64
        buffered = BytesIO()
        img.save(buffered, format="JPEG")
        image_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')

    request_id = str(uuid.uuid4())

    # Prompt text for the Gemini API
    # Refactor this promp to match the arvolaskuri requirements. You can also use structured output to get the result in a structured format. https://ai.google.dev/gemini-api/docs/structured-output?lang=python
    prompt = f"""
        Request ID: {request_id}

        Analyze the furniture piece in this image. Determine the following attributes:
        - Type of furniture
        - Brand (if visible or recognizable)
        - Model (if visible or recognizable)
        - Color
        - Approximate dimensions (length, width, and height) in cm
        - Estimated age
        - Condition

        Provide this information in JSON format. Include the request_id in your response.
        If there is no furniture in the picture, return an error message.
        """

    # Process the response from Gemini API
    try:
        # Specify the model version. Check the available models here: https://ai.google.dev/gemini-api/docs/models/gemini
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(
            [prompt, {'mime_type': 'image/jpeg', 'data': image_base64}])

        result = response.text.strip(" ```\n").replace(
            "json\n", "", 1).replace("JSON\n", "", 1)

        return json.loads(result)
    except Exception as e:
        logger.error(f"An unexpected error occurred: {str(e)}")
        return {"error": "An unexpected error occurred."}


if __name__ == "__main__":
    # Path to local image file
    image_path = "akademia.png"  # example image

    # Check if the file exists
    if not os.path.exists(image_path):
        print(f"Error: The file {image_path} does not exist.")
    else:
        # Call the analyze_image function
        result = analyze_image(image_path)
        print(json.dumps(result, indent=2))
