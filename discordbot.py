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
    if message.content.startswith('hello'):
      await message.channel.send("Hello"+ " " + message.author.mention)
    if message.content.startswith('meme'):
      await message.channel.send(get_meme()+ " " + message.author.mention)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTM3NzI1NTA4Njg3NDY4OTY1OA.GcaJds.dqE_w7KZeR0O3pbwM5t31wLheQ4npTx1VE8GZ4') # Replace with your own token.