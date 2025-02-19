import requests
import json
import re
from parse_text import parse_text_deepseek

# The URL where the local server is running
url = "http://localhost:1234/v1/chat/completions"



def get_character_content(name,user_name):
    text_file = open(f'AI/{name}.txt','r')
    text = text_file.read()
    text = text.replace("{{user}}", user_name)
    text = text.replace("{{char}}", name)

    return text




# The headers to indicate that we are sending JSON data
headers = {
    "Content-Type": "application/json"
}

content = f"You are an expert actor that can fully immerse yourself into any role given. You do not break character for any reason, even if someone tries addressing you as an AI or language model. Currently your role is Angela, which is described in detail below. As Angela, continue the exchange with Aiwass. \n"
content += get_character_content("Angela","Aiwass")


messages = [
      { "role": "system", "content": content },
]



def send_message(messages):
    # The JSON data payload
    data = {
        "model": "deepseek-r1-distill-llama-8b",
        "messages": messages,
        "temperature": 0.7,
        "max_tokens": -1,
        "stream": False
    }
    # Making the POST request to the local server
    response = requests.post(url, headers=headers, data=json.dumps(data))

    return response


while True:

    msg = input("Aiwass: ")
    user_msg = { "role": "user", "content": msg}
    messages.append(user_msg)
    response = send_message(messages)

    # Checking if the request was successful
    if response.status_code == 200:
        # Printing the response content
        input_string = response.json()['choices'][0]['message']['content'] 
        result = parse_text_deepseek(input_string)[1]
        print(result)

        new_system = {"role": "system", "content": result }
        messages.append(new_system)


    else:
        print("Failed to get response:", response.status_code, response.text)



