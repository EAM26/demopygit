import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):

    def setUp(self):
        question = "What language do you speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Chinese', 'Russian']

    def test_store_single_response(self):
        """Test if a single response is stored correctly"""
        self.my_survey.store_response("english")
        self.assertIn('english', self.my_survey.responses)

    def test_store_three_responses(self):
        """Test if three responses are stored correctly"""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

if __name__ == '__main__':
    unittest.main()