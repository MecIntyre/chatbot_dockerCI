import unittest
from chatbot_ai import Chatbot


class TestChatBot(unittest.TestCase):
    def test_intelligent_answers(self):
        """Test der intelligenten Antworten"""
        self.__reaktionen = {"hallo": "aber hallo",
                    "geht": "Was verstehst Du darunter",
                    "schmeckt": "Ich habe keinen Geschmackssinn"}
        __data = ["hallo du", "geht es dir gut", "schmeckt die Suppe"]
        __bot = Chatbot(self.__reaktionen)
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
