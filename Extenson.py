from discord.ext.commands import Bot
import random



BOT_PREFIX = ("")
TOKEN = "<TOKEN>"

client = Bot(command_prefix=BOT_PREFIX)

@client.command(name="Tell-me-about-saurabh")
async def friend1():
    possible_responses = [ 
        'WO THO BADA CHUTIYA HAI!',
        'INTELLIGNET AS FUCK HAI!',
        'SALEY MEY SHARAM HI NAHI HAI!',
        'KITINA PADATOBHI SATISFIED NAHI HAI!',
    ]
    await client.say(random.choice(possible_responses))

@client.command()
async def friend2():
    possible_responses = [ 
        'WO THO BADA CHUTIYA HAI!',
        'INTELLIGNET AS FUCK HAI!',
        'SALEY MEY SHARAM HI NAHI HAI!',
        'KITINA PADATOBHI SATISFIED NAHI HAI!',
    ]
    await client.say(random.choice(possible_responses))
    
@client.command()
async def friend3():
    possible_responses = [ 
        'WO THO BADA CHUTIYA HAI!',
        'INTELLIGNET AS FUCK HAI!',
        'SALEY MEY SHARAM HI NAHI HAI!',
        'KITINA PADATOBHI SATISFIED NAHI HAI!',
    ]
    await client.say(random.choice(possible_responses))
    

@client.command()
async def friend4():
    possible_responses = [ 
        'WO THO BADA CHUTIYA HAI!',
        'INTELLIGNET AS FUCK HAI!',
        'SALEY MEY SHARAM HI NAHI HAI!',
        'KITINA PADATOBHI SATISFIED NAHI HAI!',
    ]
    await client.say(random.choice(possible_responses))

client.run(TOKEN)