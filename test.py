import configparser
import google.ai.generativelanguage as glm
import json
import re

#pip install google.ai.generativelanguage
class StoryBuilder():
    def __init__(self):
        with open('config.json') as f:
            config = json.load(f)
        API_KEY = config['API_KEY']    
        self.client = glm.DiscussServiceClient(client_options={'api_key': API_KEY})
        self.context = "In Chat mode act as a story teller and Develop an interactive storytelling game where users can become characters in a virtual world and make decisions that shape the outcome of the story. There should be just 1 story would with  10 conversation long where you'd generate a story with 3 options and user would select an option and story would proceeed that way.Proceed step by step. Also let users have the freedom to enter their own choice."
    
    def send_message(self):
        while True:
            user_input = input("Enter your message: ")
            request = glm.GenerateMessageRequest(model='models/chat-bison-001', 
                        prompt=glm.MessagePrompt(
                        messages=[glm.Message(content=user_input)], context=self.context))
            response_obj = self.client.generate_message(request)
            response = ((str(response_obj.candidates)))
            print(response)
    
obj = StoryBuilder()
obj.send_message()
