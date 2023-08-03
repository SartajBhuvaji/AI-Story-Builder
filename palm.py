import google.generativeai as palm
import json

class StoryBuilder():
    def __init__(self):
        with open('config.json') as f:
            config = json.load(f)
        API_KEY = config['API_KEY']   
        palm.configure(api_key=API_KEY)
        prompt = " Start with asking for a Story Type like Mystery, Romance, Sci-Fi, Fantasy, Horror, Thriller, Western, Adventure, Comedy, Drama, Action, Children, and Non-Fiction."
        context = "Act as an interactive story developer that would create 3 part of story. You'd generate the first part of the story and give the user 3 options/actions to choose from for the next part of the story. (This makes the story interactive.) Once the user selects the option.action. You'd generate the next part of the story based on the action selected by the user. For the final part once the user selects an option, you'd conclude the story as building on the selected option and concluding the story. The story should have a protoganist and an antogonist.  The story should be creative and imaganitive."
        self.response = palm.chat(messages = prompt, temperature = 0.2, context = context)
        print(self.response.last)

    def converse(self):
            while True:
                user_input = input("Enter your message: ")
                self.response = self.response.reply(user_input)
                print(self.response.last)


obj = StoryBuilder()
obj.converse()