import os
from dotenv import load_dotenv
from google import genai


# Load environment variables from the .env file
load_dotenv()


# Initialize the Gemini client 
# It automatically picks up the GEMINI_API_KEY environment variable
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY_X"))


# user inputs a prompt to the model and gets a response
promt = input("Enter your promt: ")

# Generate a quick test response
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=promt, 
)

print()
print("...Getting response from Gemini API...")
print()
print(response.text)

