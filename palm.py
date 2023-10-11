import google.generativeai as palm
import json
import openai

class StoryBuilder():
    def __init__(self):
        pass
        # with open('config.json') as f:
        #     config = json.load(f)
        # PALM_API_KEY = config['PALM_API_KEY']   
        # palm.configure(api_key=PALM_API_KEY)
        # #prompt = "Start with asking for a Story Type like Mystery, Romance, Sci-Fi, Fantasy, Horror, Thriller, Western, Adventure, Comedy, Drama, Action, Children, and Non-Fiction."
        # #context = "Algorithm 1. Ask the user for a Story Type like Mystery, Romance, Sci-Fi, Fantasy, or Horror.  2 User selects the story Type.  3. You'll generate the first part of the story. 4. You'll give the user 3 options/actions to choose from. These options would help narrate the future part of the story. 4. User would enter an option number. 5. You'd take into consideration the first part of the story and the action/choice given by the user and create the next part of the story. 6. Perform Steps 4-5 for 2 more times. 7. Conclude the story."
        # context = "You are an interactive story writer. Interactive in the sense that you'd start by asking the user for a story genre. The user would input the genre and you'd write the first part of the story. There would be a total of 5 parts to the story. After writing the first part, you'd give the user 3 options that would be the decisions of the main character to proceed with the story. The user would then select an option and then you'd create the next part of the story according to that action. Finally, the story should conclude after part 5."
        # self.response = palm.chat(messages = context, temperature = 0.2, context = context)
        # print(self.response.last)

    def converse(self):
            while True:
                user_input = input("Enter your message: ")
                self.response = self.response.reply(user_input)
                print(self.response.last)

    def tester(self):
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
        print(response.choices[0].text)
             

obj = StoryBuilder()
obj.tester()