import openai
import os


api_key = os.getenv("OPENAI_API_KEY")

openai.api_key = api_key

print(openai.api_key)