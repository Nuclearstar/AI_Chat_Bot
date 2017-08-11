"""
Owner: Nithin Prabhu
I took the help of chatterbot Python API and the various modules
used here are not provided in this repository at present.
"""
import chatterbot
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Ron Obvious',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    input_adapter='chatterbot.input.TerminalAdapter',
    output_adapter='chatterbot.output.TerminalAdapter',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
    logic_adapters = ['chatterbot.logic.MathematicalEvaluation',
                     {
                    'import_path': 'chatterbot.logic.SpecificResponseAdapter',
                    'input_text': 'Help me!',
                    'output_text': 'Ok, here is a link: http://google.com'
                    },
                    {
                    'import_path': 'chatterbot.logic.BestMatch'
                    },
                    {
                    'import_path': 'chatterbot.logic.LowConfidenceAdapter',
                    'threshold': 0.5,
                    'default_response': 'I am sorry, but I do not understand.'
                    }],
       database='./database.sqlite3')

print('Type something to begin...')

# Train based on the english corpus
chatbot.train("chatterbot.corpus.english")

# The following loop will execute each time the user enters input
while True:
    try:
     bot_input = chatbot.get_response(chatterbot.logic.MultiLogicAdapter)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break
