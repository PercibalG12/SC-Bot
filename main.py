import discord
import os 
from dotenv import load_dotenv
import nltk
from neuralintents import GenericAssistant
nltk.download("omw-1.4")
nltk.download("punkt")
nltk.download("wordnet")

chatbot = GenericAssistant('intents.json')
chatbot.train_model()
chatbot.save_model()

print("Bot is running!")

client = discord.Client()

load_dotenv()
TOKEN = os.getenv('TOKEN')

@client.event
async def on_message(message):
    if message.author ==client.user:
              return
    if  message.content.startswith("$scbot"): 
         response = chatbot.request(message.content[7:])
         await message.channel.send(response)



client.run(TOKEN)
