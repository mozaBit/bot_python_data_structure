from discord.ext import commands
import discord
from data_structures.Linked_list import LinkedList
import os
import dotenv
# Load the token from the .env file
dotenv.load_dotenv()
token = os.getenv('TOKEN')

intents = discord.Intents.all() # Enable all intents

client = commands.Bot(command_prefix = '!', intents = intents) # Create a bot

history = LinkedList()
history.load_from_file('command_history.json')

@client.command(name='last')
async def history_last(ctx):
    last_command = history.get_last_command()
    if last_command is not None:
        await ctx.send(last_command.content)

@client.command(name='history')
async def history_user(ctx):
    user_id = ctx.author.id
    user_commands = history.get_user_commands(user_id)
    if len(user_commands) > 0:
        for command in user_commands:
            await ctx.send(command.content)

@client.command(name='back')
async def history_back(ctx):
    history.move_back()

@client.command(name='next')
async def history_forward(ctx):
    history.move_forward()

@client.command(name='clear_history')
async def history_clear(ctx):
    history.clear()

@client.command(name='purge_conv')
async def delete(ctx, amount: int = 100):
    await ctx.channel.purge(limit = amount + 1)

@client.command(name='shutdown')
@commands.is_owner()
async def shutdown(ctx):
    """Shutdown the bot."""
    await ctx.client.logout()

@client.event
async def on_message(message):
    if message.content.lower().startswith('hello'):
        await message.channel.send('Hello!')
    await client.process_commands(message)

@client.event
async def on_message(message: discord.Message):
    if message.author.bot:  # ignore messages from bots
        return
    if message.content.lower().startswith('hello'):
        await message.channel.send('Hello!')
    await client.process_commands(message)

@client.event
async def on_disconnect():
    history.save_to_file('command_history.json')

@client.listen()
async def on_message(message):
    if message.author.bot:
        return
    history.append(message)

client.run(token)
