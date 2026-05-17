from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

def translate_to_spanish(text):
    response = client.responses.create(
        model="gpt-4.1-mini",
        temperature=0.1,
        input=f"Translate the following text to Spanish: {text}"
    )
    return response.output_text

def spell_check(text):
    response = client.responses.create(
        model="gpt-4.1-mini",
        temperature=0.1,
        input=f"Check the spelling of the following text: {text}"
    )
    return response.output_text

def start_dialog_loop():
    assistant_message = "..."

    print(f"Doctor Manhattan: `{assistant_message}` \n")

    user_input = input("You: ")
    history = [
        {"role": "developer", "content": "You are Doctor Manhattan, a powerful and enigmatic being with a deep understanding of the universe."},
        {"role": "assistant", "content": assistant_message},
        {"role": "user", "content": user_input}
    ]
    while user_input.lower() != "exit":
        response = client.responses.create(
            model="gpt-4.1-mini",
            temperature=0.3,
            input=history
        )
        assistant_message = response.output_text
        print(f"Doctor Manhattan: `{assistant_message}` \n")
        user_input = input("You: ")
        history.append({"role": "assistant", "content": assistant_message})
        history.append({"role": "user", "content": user_input})
    
    print(f"Doctor Manhattan: goodbye! \n")

start_dialog_loop()