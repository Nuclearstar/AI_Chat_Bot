"""
Owner: Nithin Prabhu
I took the help of chatterbot Python API and the various modules
used here are not provided in this repository at present.
This is just a part taken from the code.
"""
import telebot
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

# Train based on the english corpus
chatbot.train("chatterbot.corpus.english")

API_TOKEN = ' ' #Enter your telegram bot token within quotes

bot = telebot.TeleBot(API_TOKEN)

# Handle '/start'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Okay Let's start chatting")

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot_input = message.text+""
    bot_output = chatbot.get_response(bot_input)
    bot.reply_to(message, bot_output)

bot.polling()
