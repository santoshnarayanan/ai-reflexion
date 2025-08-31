from dotenv import load_dotenv
import os

load_dotenv()

def main():
    print("Hello from ai-reflexion!")
    print(os.environ.get("OPENAI_API_KEY"))


if __name__ == "__main__":
    main()
