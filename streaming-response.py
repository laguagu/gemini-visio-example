import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_stream(prompt):
    try:
        print("Trying to create response...")
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            stream=True
        )
        print("Response created. Streaming response...")

        # Loop through the response chunks
        for chunk in response:
            # Check if the chunk has content and yield it
            if chunk.choices and chunk.choices[0].delta.content is not None:
                yield chunk.choices[0].delta.content

    except Exception as e:
        print(f"Error: {str(e)}")


def main():
    prompt = input("Give prompt: ")
    print("Answer:")
    response_received = False

    # Generate and print the response stream
    for text in generate_stream(prompt):
        print(text, end='', flush=True)
        response_received = True
    print()

    if not response_received:
        print("Vastausta ei saatu. Tarkista API-avain ja mallin nimi.")


if __name__ == "__main__":
    main()
