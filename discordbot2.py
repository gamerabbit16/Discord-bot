import discord
import glob, random
import time
import requests
import json

def get_quote():
  response = requests.get('https://zenquotes.io/api/quotes/q')
  json_data = json.loads(response.text)
  return json_data

file_path_type = ["C:/Users/PC/iCloudDrive/Stuff/*.mp4","C:/Users/PC/iCloudDrive/Stuff/*.png", "C:/Users/PC/iCloudDrive/Stuff/*.jpeg"]
images = glob.glob(random.choice(file_path_type))
videopath = "C:/Users/PC/iCloudDrive/Stuff/*.mp4"
video = glob.glob(videopath)

class MyClient(discord.Client):
    async def on_ready(self):
        activity = discord.Game(name="MEMES ! MEMES ! MEMES !", type=3)
        await client.change_presence(status=discord.Status.online, activity=activity)
        print('Logged on as {0}!'.format(self.user))
    
    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith('memes'):
            random_image = random.choice(images)
            if not random_image.endswith(('.png', '.jpeg', '.jpg')):
                return
            await message.channel.send(file=discord.File(random_image))
        if message.content.startswith('video memes'):
            random_video = random.choice(video)
            if not random_video.endswith('.mp4'):
                return
            await message.channel.send(file=discord.File(random_video))
        if message.content.startswith('memes dump'):
            while True:
                random_image = random.choice(images)
                if not random_image.endswith(('.png', '.jpeg', '.jpg')):
                    return
                if message.content.startswith("STOP") or message.content.startswith("stop"):
                    break
                await message.channel.send(file=discord.File(random_image))
        if message.content.startswith("quote"):
            await message.channel.send(get_quote())



intents = discord.Intents.default()
client = MyClient(intents=intents)

client.run('token') # Replace with your own token.