'''ayu1998_agent
CSE 415, Winter 2020, Assignment 1
Yen-Chu Yu
'''
import chatbot

math_rules = [
    (r"you like (.*)", ["I like algebra!", "I like geometry!", "I love math!!"]),
    (r"(?i)what is (1\+1|one plus one)(.*)", ["Is it 3? Wait, it's 2!"]),
    (r"(.*) (plus|add) (.*)", ["Addition is involved."]),
    (r"(.*) (minus|subtract) (.*)", ["Subtraction is involved."]),
    (r"(.*) (times|multiply) (.*)", ["Mutiplication is involved."]),
    (r"(.*) (divide) (.*)", ["Division is involved."]),
    (r"(?i)(what is|can you) (.*)", ["Sorry, I'm not capable of that yet."]),
    (r"(?i)how (.*)", ["Maybe applying the distribution law works.",
                       "Maybe applying the associative law works.",
                       "Maybe applying the commutative law works."]),
    (r"(?i)math", ["Did you say something about math, I'm down for it!!"]),
    (r"", ["Continue on...", "I'm interested..."])
]
you_me = {'I':'you', 'me':'you','you':'me','am':'are',
          'mine':'yours','my':'your','yours':'mine','your':'my'}
intro_string = '''Hello! I am Math-Bot. I am a young bot who really likes
to talk about math regardless to your input.'''


InfoSciAgent = chatbot.chatbot(math_rules, you_me, "Info-Expert", intro_string)

if __name__=="__main__":
    InfoSciAgent.chat()
