import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('API_KEY')

def translate_to_sith(text):
    url = "https://sith.p.rapidapi.com/sith.json"
    headers = {
        "x-rapidapi-key": api_key,
        "x-rapidapi-host": "sith.p.rapidapi.com"
    }
    params = {"text": text}
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return data["contents"]["translated"]  # Extract only the translated text
    else:
        return f"Error: {response.status_code}, {response.text}"

if __name__ == "__main__":
    while True:
        user_text = input("Enter a sentence to translate into Sith (or type 'exit' to quit): ")
        if user_text.lower() in ["exit", "quit"]:
            print("Goodbye! May the Dark Side guide you.")
            break  # Exit the loop
        
        sith_translation = translate_to_sith(user_text)
        print("Sith Translation:", sith_translation)
