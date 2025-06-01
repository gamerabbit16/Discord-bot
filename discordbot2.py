import discord
import glob, random
import time
import requests
import json

# Fetch a random quote from ZenQuotes API and a NASA image of the day

response = requests.get('https://zenquotes.io/api/today/q').json()

datata = requests.get("https://api.nasa.gov/planetary/apod?api_key=your nasa token").json()

file_path_type = ["path/*.mp4","path/*.png", "path/*.jpeg"]
images = glob.glob(random.choice(file_path_type))
videopath = "path/*.mp4"
video = glob.glob(videopath)

url = datata["url"]  # Replace with your image URL
image_content = requests.get(url).content
with open("nasaimages.png", "wb") as nasaimage:
    nasaimage.write(image_content)

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
            await message.channel.send(response[0]['q'] + " - " + response[0]['a'])
        if message.content.startswith("nasa image"):
            if "url" in datata:
                url = datata["url"]  # Replace with your image URL
                image_content = requests.get(url).content
                with open("nasaimages.png", "wb") as nasaimage:
                    nasaimage.write(image_content)
                await message.channel.send(file=discord.File("nasaimages.png"))
            else:
                await message.channel.send("Error: 'url' key not found in NASA API response.")


intents = discord.Intents.default()
client = MyClient(intents=intents)

client.run('Token') # Replace with your own token.