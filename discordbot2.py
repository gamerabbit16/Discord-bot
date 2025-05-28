import discord
import glob, random
import time

file_path_type = ["PATH/*.mp4","PATH/*.png", "PATH/*.jpeg"]
images = glob.glob(random.choice(file_path_type))
videopath = "C:/Users/PC/iCloudDrive/Stuff/*.mp4"
video = glob.glob(videopath)

class MyClient(discord.Client):
    async def on_ready(self):
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

intents = discord.Intents.default()


client = MyClient(intents=intents)
client.run('token') # Replace with your own token.