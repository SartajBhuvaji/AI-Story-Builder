import google.generativeai as palm
import json
import openai 

with open('config.json') as f:
            config = json.load(f)
openai.api_key = config['CHAT_GPT_API_KEY']
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role":"user", "content":"How are you doing?"}]
    # temperature=0.9,
    # max_tokens=150,
    # top_p=1,
    # frequency_penalty=0.0,
    # presence_penalty=0.6,
)
print(response.choices[0].message.content)
        