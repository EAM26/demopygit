class AnonymousSurvey:

    def __init__(self, question):
        """store question and create list for responses"""
        self.question = question
        self.responses = []


    def show_question(self):
        """show question to user"""
        print(f"{self.question} ")


    def store_response(self, new_response):
        """store response in list"""
        self.responses.append(new_response)


    def show_responses(self):
        print("Results Survey:")
        for response in self.responses:
            print(f" - {response.title()}")


