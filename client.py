
from openai import OpenAI
# pip install openapi

client = OpenAI()
# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="sk-proj-GB26aGqn6DrYTfqT07GiT3BlbkFJcu5QwQ6EQMOZfFd8QK49",
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtua assistance named jarvis skilled in general tasks like alexa and Google Cloud"},
    {"role": "user", "content": "What is coding"}
  ]
)

print(completion.choices[0].message)