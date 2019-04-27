import discord
from discord.ext.commands import Bot

TOKEN = 'NTcxNDgyNTMyMjY5MzkxOTEz.XMOeJg.5sOWsJt0MTbuiEsIRkrIE5AVsXs'

BOT_PREFIX = ('+','!')

client = Bot(command_prefix=BOT_PREFIX)

bot.command(pass_context=True)
async def slap(member: discord.Member):
        """<member>: Be careful with this one."""
        await bot.say("{} slaps {} around a bit with a large trout.".format(ctx.message.author.mention, member.mention))

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
client.run(TOKEN)