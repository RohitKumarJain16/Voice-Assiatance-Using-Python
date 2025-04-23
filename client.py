import openai
import os

# Load the API key from an environment variable
openai.api_key = os.getenv("Enter API Key")

# Create a response using the correct method and model
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": "Write a one-sentence bedtime story about a unicorn."}
    ]
)

# Print the response
print(response['choices'][0]['message']['content'])