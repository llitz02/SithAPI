import http.client
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Access environment variables
api_key = os.getenv('API_KEY')


# Define a function to handle the API call
def translate_to_sith(text):
    conn = http.client.HTTPSConnection("sith.p.rapidapi.com")
    headers = {
        'x-rapidapi-key': "API_KEY",  
        'x-rapidapi-host': "sith.p.rapidapi.com"
    }
    # Replace spaces in the text with %20 for URL encoding
    conn.request("GET", f"/sith.json?text={text.replace(' ', '%20')}", headers=headers)
    
    res = conn.getresponse()
    data = res.read()
    
    # Return the decoded response
    return data.decode("utf-8")

# Main logic to get user input and display the result
if __name__ == "__main__":
    user_text = input("Enter the sentence you want to translate into Sith: ")
    sith_translation = translate_to_sith(user_text)
    print("Sith Translation:", sith_translation)
