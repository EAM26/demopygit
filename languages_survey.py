from survey import AnonymousSurvey

my_survey = AnonymousSurvey("What language do you speak?")
my_survey.show_question()

while True:
    response = input("Type in language or 'q' to quit: ")
    if response == 'q':
        my_survey.show_responses()
        break
    else:
        my_survey.store_response(response)