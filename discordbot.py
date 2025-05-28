import discord
import requests
import json

def get_meme():
  response = requests.get('https://meme-api.com/gimme')
  json_data = json.loads(response.text)
  return json_data['url']

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

  async def on_message(self, message):
    if message.author == self.user:
      return
    if message.content.startswith('hello') and not message.content.endswith('meme'):
      await message.channel.send("Hello"+ " " + message.author.mention)
    if message.content.startswith('meme'):
      await message.channel.send(get_meme()+ " " + message.author.mention)
    if message.content.startswith('hello') and message.content.endswith('meme'): #if it start with hello and end with meme is send a hey message and a meme
      await message.channel.send("hello " + message.author.mention + " " +get_meme())


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('your toke here') # Replace with your own token.