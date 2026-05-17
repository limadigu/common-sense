from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()
response = client.responses.create(
    model="gpt-4.1-mini",
    temperature=0.1,
    input="What rock band/artist is considered to be the biggest of every decade since the 1950s?"
)

print(response.output_text)