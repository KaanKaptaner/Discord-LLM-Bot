import os
import discord
from discord.ext import commands
from langchain_community.llms import Ollama
from crewai import Agent, Task

os.environ["OPENAI_API_BASE"] = 'https://api.groq.com/openai/v1'
os.environ["OPENAI_MODEL_NAME"] ='llama3-8b-8192'  # Adjust based on available model
os.environ["OPENAI_API_KEY"] ='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'

llm = Ollama(model="llama3")



class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return
        
        if message.content.startswith('!'):
        # Remove the command from the message
            striptted_message = message.content[len('!'):].strip()
            await message.channel.send(llm.invoke(striptted_message, stop=['<|eot_id|>']))



intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('ODk4NTA3MzkzOTA0ODAzODcw.GHLXSO.M4e0Yxy0Vx6_629tf5fGy0qxDtH0XLLAHwSMM4')