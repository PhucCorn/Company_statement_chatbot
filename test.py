import os

open_ai_key = os.getenv('OPENAI_API_KEY')
print(open_ai_key)

def find_env_file(directory="."):
    for root, dirs, files in os.walk(directory):
        if ".env" in files:
            return os.path.join(root, ".env")
    return None

env_path = find_env_file()
print(f"Path to .env file: {env_path}")
