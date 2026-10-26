from time import time

from dotenv import load_dotenv
from google import genai

load_dotenv()


def main() -> None:
    user_input = input("Enter your prompt: ")
    client = genai.Client()

    interaction = client.interactions.create(
        model="gemini-3.8-flash",
        input=user_input,
        system_instruction="You are friendly and funny person.",
    )
    print(interaction.output_text)


if __name__ == "__main__":
    start = time()
    main()
    end = time()
    print(f"Execution time: {end - start} seconds")
