import nltk
import random
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"what is your name?",
        ["I am a simple chatbot.",]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm fine, how about you?",]
    ],
    [
              r"sorry (.*)",
        ["It's alright", "No problem",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that", "That's great!",]
    ],
    [
        r"hi|hello|hey",
        ["Hello", "Hey there", "Hi!",]
    ],
    [
        r"(.) (weather|temperature) in (.)",
        ["I am not equipped to provide real-time weather information for %3. You might want to check a weather website or app.",]
    ],
    [
        r"(.) (time) in (.)",
        ["I do not have access to the current time in %3. Please check your device's clock.",]
    ],
    [
        r"quit|bye|goodbye|see you",
        ["Goodbye!", "Have a great day!", "See you later.",]
    ],
    [
        r"(.*)",
        ["I'm not sure I understand. Can you please rephrase?",]
    ],
]
chatbot = Chat(pairs, reflections)

def basic_chatbot():
    print("Hello! I'm a basic chatbot. Type 'quit' to exit.")
    chatbot.converse()

if __name__ == "__main__":
 basic_chatbot()
