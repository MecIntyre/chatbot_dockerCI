import unittest
from chatbot_ai import Chatbot_ai
from chatbot_ai import nltk
from chatbot_ai import training
from chatbot_ai import output
from chatbot_ai import pickle
from chatbot_ai import f


class TestChatBot(unittest.TestCase):
    def test_intelligent_answers(self):
        jsonFile = "v3/intents.json"
        with open(jsonFile):
            """Test der intelligenten Antworten"""
            self.__reaktionen = {"greetings": "Hallo",
                        "goodbye": "Sehe Dich später",
                        "age": "wie alt ist Jörg",
                        "name": "Wie ist Dein Name",
                        "shop": "Heute gibt es Kekse!",
                        "hours": "Wann ist die Öffnungszeit"}
            __data = ["Guten Tag", "Tschö", "Wie alt bist Du"]
            __bot = Chatbot_ai(jsonFile)
        try:
            pickle.dump((self.words, self.labels, training, output), f)
        except Exception:
            self.words = []
            self.labels = []

            for sentence in __data:
                __bot.set_Message(sentence)
                self.__response = __bot.get_response()
                __words = sentence.split()
                for word in __words:
                    if word in self.__reaktionen:
                        self.__rightResponse = self.__reaktionen[word]
            self.assertEqual(self.__response, self.__rightResponse)


if __name__ == '__main__':
    unittest.main()
