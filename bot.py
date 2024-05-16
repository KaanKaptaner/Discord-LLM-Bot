import os
import discord
from groq import Groq

client = Groq(api_key=os.getenv('GROQ_API_KEY'))

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        global active
        
        if message.author == bot.user:
            return

        if message.content.lower() == '!activate':
            active = True
            await message.channel.send('Bot activated!')
        elif message.content.lower() == '!deactivate':
            active = False
            await message.channel.send('Bot deactivated!')
        
        if message.author.id == self.user.id:
            return
        if active:
            if message.content.startswith(''):
                stripped_message = message.content[len(''):].strip()
                chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": stripped_message,
                    }
                ],
                model="llama3-8b-8192",
            )
            if chat_completion.choices:
                await message.channel.send(chat_completion.choices[0].message.content)
            else:
                await message.channel.send("No completion choices returned.")



intents = discord.Intents.default()
intents.message_content = True

bot = MyClient(intents=intents)
bot.run(os.getenv('DISCORD_TOKEN'))
