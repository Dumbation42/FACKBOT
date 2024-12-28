import discord
import asyncio
import random

#Where to get bot token
  #https://discord.com/developers/applications

#How to get Channel ID
#https://discover.hubpages.com/technology/Discord-Channel-ID

# Replace with your bot's token
BOT_TOKEN = 'DISCORD-BOT-TOKEN'

# Replace with your channel ID
CHANNEL_ID = CHANNELID

LYRICS = [
    "Ow, ow, ow (Oh, goddamn)",
    "I'm gonna facking cum (Oh, shit)",
    "Fack, fack, fack (Fuck, I am)",
    "I am, I'm going to cum (I'm cumming)",
    "(Oh, yeah, God) I never seen no chick like this",
    "This bitch can twist like a damn contortionist",
    "Condom on my dick? Of course it is",
    "This bitch don't know what abortion is",
    "So I can't cum in her, fucks like a porn star",
    "Looks like Jenna, fack, I'm gonna",
    "Cum, I think my rubber's comin' off",
    "But, oh, it's so fucking wet and soft",
    "Fuck, I'm gonna start lettin' off",
    "I'm squirting and she's not gettin' off",
    "And she's on top, I'm gonna facking",
    "Oh, God, oh, don't do that",
    "Don't, stop, stop, don't, I don't mean 'don't stop'",
    "Ow, wait a minute, ow, ow, fuck",
    "I, I'm gonna fucking cum (*Squirt squirt squirt*)",
    "Ow, ow, ow (Oh, goddamn)",
    "I'm gonna fucking cum (Oh, shit)",
    "Fack, fack, fack (Fuck, I am)",
    "I am, I'm going to cum (I'm cumming)",
    "(Oh, yeah, God) Ooh, wow, boom that pow",
    "Ooh, ow, I need a cigarette now",
    "Ow, I'm so fucking hot",
    "And you're so fucking hot",
    "Oh my God, I wanna facking fack",
    "No, not 'fuck,' I said 'fack'",
    "F-A-C-K, F-A-C-K",
    "Fack, fack, fack, facking freak me",
    "Oh yeah, girl, see, baby, they call me Mr. Freaky",
    "Let's call your sister, three-way",
    "Have some threesome, me so horny",
    "And you're such a fucking babe",
    "I wanna go down on you—fuck, you shaved?",
    "Oh, goddamn, here I go again",
    "I'm gonna cum, I am",
    "Ow, ow, ow (Oh, goddamn)",
    "I'm gonna facking cum (Oh, shit)",
    "Fack, fack, fack (Fuck, I am)",
    "I am, I'm going to cum (I'm cumming)",
    "I'm Slim Shady, uh, uh, uh",
    "Okay, I'm done, I already came twice",
    "You ain't gonna make me cum",
    "I'm all outta gas, not so fast",
    "Uh, your finger just went in my ass",
    "Ow, that hurts, take it out now!",
    "Oh, wait a minute, aw",
    "Put it back in, in, in, in",
    "This don't mean I'm gay, I don't like men",
    "I like boobs, boobs, boobs",
    "Now, see that gerbil? Grab that tube",
    "Shove it up my butt",
    "Let that little rascal nibble on my asshole, uhh",
    "Yeah, right there, right there",
    "Ahh, I'm cumming, oh, yeah",
    "Fack, I just came again",
    "Okay, pull it out now, enhh",
    "Oh, fuck yeah",
    "Wait, he's not out, he's still crawling around up there",
    "Ow, fuck, I think it's stuck",
    "Ow, but it feels so fucking good",
    "Shove a gerbil in your ass through a tube",
]

CELEBRATION_EMOJI = "🎉"

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}!')
    channel = client.get_channel(CHANNEL_ID)
    if channel is None:
        print("Channel not found! Please check the CHANNEL_ID.")
        return

    while True:
        try:
            message_content = random.choice(LYRICS)

            message = await channel.send(message_content)

            if message_content == "I like boobs, boobs, boobs":
                await channel.send("@everyone I like boobs, boobs, boobs!")
                await message.add_reaction(CELEBRATION_EMOJI)

            await asyncio.sleep(random.randint(1, 5))
        except Exception as e:
            print(f"An error occurred: {e}")
            break

client.run(BOT_TOKEN)
