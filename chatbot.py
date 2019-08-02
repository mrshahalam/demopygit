from chatterbot import  ChatBot
from chatterbot.trainers import  ListTrainer
conversation=[
    'Hellow',
    'hi there',
    'how r u doing',
    'i m doinng great',
    'that is good to here'
    'what is your name',
    'My name is Charlie',
    'whats app',
    'no thing special',
    'what are you doing',
    'i am here to help u',
    'What is your father name',
    'my father name is shah alam',
    'thank you'
]
chatbot=ChatBot('Bisp')
chatbot.set_trainer(ListTrainer)
chatbot.train(conversation)
while True:
    userinput=input('You:')
    if userinput=='bye' or userinput.strip()=='bye':
        print('ChatBot:Bye')
        break;
    else:
        response=chatbot.get_response(userinput)
        print('ChatBot:',response)
