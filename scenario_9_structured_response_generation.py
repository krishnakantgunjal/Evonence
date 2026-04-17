from google import genai
import json

client = genai.Client(api_key="API_KEY")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents='Give response in JSON: List 3 benefits of Python for data science.'
)

try:
    data = json.loads(response.text)
    print(data)
except:
    print("Invalid JSON response")
