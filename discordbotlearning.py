import discord # type: ignore
from discord.ext import commands
import time
intents=discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="|",intents=intents)

hicounter=0
def count():
    global hicounter
    hicounter+=1
    if hicounter == 3:
        hicounter=1
    return hicounter

hscounter=0
def count():
    global hscounter
    hscounter+=1
    if hscounter == 3:
        hscounter=1
    return hscounter

def stopwatch(seconds):
    start = time.time()
    time.perf_counter()    
    elapsed = 0
    while elapsed < seconds:
        elapsed = time.time() - start
        print ("loop cycle time: %f, seconds count: %02d" % (time.perf_counter() , elapsed)) 
        time.sleep(1)  

@client.event
async def on_message(message):
    if message.content.startswith('hello'):
        await message.channel.send("jello fellow!")
    if message.content.startswith('embedhello'):
        embedVar = discord.Embed(title="Hi", description="This is how you say hello in a cool way!", color=0x00ff00)
        embedVar.add_field(name="Heallo", value="hi1", inline=False)
        embedVar.add_field(name="Haello", value="hi2", inline=True)
        await message.channel.send(embed=embedVar)
    if message.content.startswith('imagehello'):
        await message.channel.send('https://images.rawpixel.com/image_png_800/cHJpdmF0ZS9sci9pbWFnZXMvd2Vic2l0ZS8yMDIzLTA1L3JtNjUxLWVsZW1lbnQtYy0wMTQtcC5wbmc.png')
    if message.content.startswith('skullreactthis'):
        await message.channel.send('https://1000logos.net/wp-content/uploads/2023/05/Skull-Emoji.png')
    if message.content.startswith('manimdead'):
        await message.channel.send('https://1000logos.net/wp-content/uploads/2023/05/Skull-Emoji.png')
        await message.channel.send("manimdead")
    if message.content.startswith('messagemyself'):
        pmuser = await client.fetch_user(message.author.id)
        await pmuser.send("This is a test and a lot of non words")















 
 
    # if message.content.startswith('hi'):
    #     count()
    #     if hicounter == 2:
    #         await message.channel.send('Hello Gentlemen!')
    # if message.content.startswith('handshake'):
    #     user = id
    #     if user == user:
            
    #         return
    #     if user != user:
    #         await message.channel.send('Deal has been made!')
    #         user = ""
    #     stopwatch(7)
    #     user = ""
        

        




client.run ('SECRET GOES HERE')
