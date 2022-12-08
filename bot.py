import discord

default_intents = discord.Intents.default()
default_intents.members = True

client = discord.Client(intents=default_intents)


@client.event
async def on_ready():
    print("Le bot est prêt.")


@client.event
async def on_member_join(member):
    general_channel: discord.TextChannel = client.get_channel(1050329969919787080)
    await general_channel.send(content=f"Bienvenue sur le serveur tafiole {member.display_name} !")


@client.event
async def on_message(message):
    if message.content.startswith("!del"):
        number = int(message.content.split()[1])
        messages = await message.channel.history(limit=1).flatten()

        for each_message in messages:
            await each_message.delete()


# @client.event
# async def on_message(message):
#     if message.content.lower() != "ping":
#         await message.channel.send("pong")


client.run("MTA1MDMyODE2ODk2NTM0OTM3Nw.GZT4Qp.AaF_YWXNC-tVumGHg8ytnIADnfx9d2GbX0ygpU")
