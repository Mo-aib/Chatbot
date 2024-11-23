# Description: This is a chatbot program to save time on FAQ about MMA before watching the sport

# Import the library
from nltk.chat.util import Chat, reflections

# Custom reflections for better conversation
custom_reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "me": "you"
}

# Filling in FAQ
pairs = [
    # General greetings
    ["(hi|hello|hey|what's up)", [
        "Hey there! Ready to talk about MMA?", 
        "Hi! What do you want to know about Mixed Martial Arts?"
    ]],
    ["My name is (.*)", [
        "Nice to meet you, %1! What MMA questions do you have?"
    ]],

    # What is MMA?
    ["What is MMA?", [
        "MMA stands for Mixed Martial Arts, a full-contact combat sport that combines techniques from various disciplines like boxing, wrestling, and Brazilian Jiu-Jitsu."
    ]],
    ["Tell me about MMA", [
        "MMA, or Mixed Martial Arts, is a combat sport that combines striking and grappling techniques from multiple martial arts disciplines. It's intense, exciting, and growing in popularity!"
    ]],

    # Disciplines involved in MMA
    ["What disciplines are involved in MMA?", [
        "MMA includes disciplines like boxing, Brazilian Jiu-Jitsu, Muay Thai, wrestling, judo, and karate."
    ]],

    # Is MMA dangerous?
    ["Is MMA dangerous?", [
        "Like any combat sport, MMA has risks. Fighters face injuries like cuts and bruises, but organizations enforce strict rules and safety measures to protect athletes."
    ]],
    ["How dangerous is MMA?", [
        "MMA is as dangerous as other contact sports. However, professional fighters are highly trained, and referees can stop fights to prevent serious injuries."
    ]],

    # What is a submission?
    ["What is a submission?", [
        "A submission in MMA is when a fighter forces their opponent to tap out using a choke or joint lock. Examples include the armbar, guillotine choke, and rear-naked choke."
    ]],
    ["Can you explain submissions?", [
        "Submissions are techniques that force an opponent to give up, often due to pain or being trapped. They're a key part of Brazilian Jiu-Jitsu and MMA strategy."
    ]],

    # Who is the best fighter?
    ["Who is the best fighter?", [
        "The 'best' fighter is subjective. Legends like Jon Jones, Georges St-Pierre, and Amanda Nunes are often in the conversation. Who do you think is the GOAT?"
    ]],
    ["(.*) best fighter (.*)", [
        "Many fans debate about the best fighter. Do you prefer striking-focused fighters like Israel Adesanya, or all-rounders like Khabib Nurmagomedov?"
    ]],

    # UFC
    ["What is the UFC?", [
        "The UFC, or Ultimate Fighting Championship, is the largest MMA organization in the world, known for hosting top-level fighters and events."
    ]],

    # Rules of MMA
    ["What are the rules of MMA?", [
        "MMA rules vary slightly by organization, but common rules include no eye-gouging, no biting, and no strikes to the back of the head. Wins can come by knockout, submission, or decision."
    ]],
    ["Explain MMA rules", [
        "In MMA, fighters must follow rules like no groin strikes or headbutts. Referees ensure safety, and rounds usually last five minutes. Want more specifics?"
    ]],

    # Weight classes
    ["How do weight classes work?", [
        "Weight classes ensure fair competition. Some examples are lightweight (155 lbs), welterweight (170 lbs), and heavyweight (205 lbs and above)."
    ]],
    ["What are MMA weight classes?", [
        "Weight classes in MMA help match fighters of similar size. Examples include featherweight (145 lbs) and middleweight (185 lbs)."
    ]],

    # Famous fighters
    ["Who are some famous MMA fighters?", [
        "Famous fighters include Conor McGregor, Khabib Nurmagomedov, Amanda Nunes, Jon Jones, and Israel Adesanya."
    ]],
    ["Tell me about famous MMA fighters", [
        "Some legendary MMA fighters are Georges St-Pierre, Ronda Rousey, and Anderson Silva. Each has made a huge impact on the sport."
    ]],

    # Where to watch MMA
    ["Where can I watch MMA fights?", [
        "You can watch MMA on platforms like ESPN, UFC Fight Pass, and pay-per-view events. Check local listings for specific events."
    ]],

    # Open-ended prompts
    ["(.*) MMA (.*)", [
        "MMA is a fascinating sport. Are you asking about its history, rules, or training methods? Let me know!"
    ]],
    ["(.*) UFC (.*)", [
        "The UFC is the biggest MMA organization. Are you curious about fighters, events, or its history?"
    ]],
    ["(.*) dangerous (.*)", [
        "MMA has risks, but fighters are highly trained, and organizations prioritize safety. Do you want details on injuries or safety measures?"
    ]],
    ["(.*) submission (.*)", [
        "Submissions are techniques used to force an opponent to tap out, like arm locks and chokes. They're a key part of MMA!"
    ]],
]

# Fallback response
def custom_converse(chatbot):
    print("Start chatting with the MMA FAQ bot! Type 'quit' to exit.")
    while True:
        user_input = input("> ")
        if user_input.lower() == "quit":
            print("Goodbye! Feel free to come back with more MMA questions.")
            break
        response = chatbot.respond(user_input)
        if response:
            print(response)
        else:
            print("Please clarify your question.")

# Create and run the chatbot
chat = Chat(pairs, custom_reflections)
custom_converse(chat)
