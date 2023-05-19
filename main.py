from discord.ext import commands # import commands from discord.py
import discord # import discord.py
from data_structures.Linked_list import LinkedList # import Linked_list class from data_structures/Linked_list.py
import os # import os module
import dotenv  # import dotenv module
# Load the token from the .env file
dotenv.load_dotenv()
token = os.getenv('TOKEN')

intents = discord.Intents.all() # Enable all intents

client = commands.Bot(command_prefix = '!', intents = intents) # Create a bot

history = LinkedList() # create a new Linked_list
messages = LinkedList() # create a new Linked_list
history.load_from_file('command_history.json') # load the command list from a file

@client.event  # create an event that sends a hello message when a user says hello
async def on_message(message: discord.Message):
    print(message.content)
    if message.author.bot:  # ignore messages from bots
        return
    if message.content.lower().startswith('hello'):
        await message.channel.send('Hello!')
    await client.process_commands(message)

@client.event  # create an event that saves the list to a file when the bot disconnects
async def on_disconnect():
    history.save_to_file('command_history.json')

@client.listen() # create a listener that adds a message to the list when a user sends a message
async def on_message(message):
    if message.author.bot:
        return
    # check if the message is a command
    if message.content.startswith('!'):
        history.append(message)
    messages.append(message)

@client.command(name='last') # create a new command last that gets the last command
async def history_last(ctx):
    last_command = history.get_last_command()
    if last_command is not None:
        await ctx.send(last_command.content)

@client.command(name='history') # create a new command history that gets all commands from a user
async def history_user(ctx):
    user_id = ctx.author.id
    user_commands = history.get_user_commands(user_id)
    if len(user_commands) > 0:
        for command in user_commands:
            await ctx.send(command.content)

@client.command(name='back') # create a new command back that moves the current node back
async def history_back(ctx):
    history.move_back()

@client.command(name='next') # create a new command next that moves the current node forward
async def history_forward(ctx):
    history.move_forward()

@client.command(name='clear_history') # create a new command clear_history that clears the list
async def history_clear(ctx):
    history.clear()

@client.command(name='purge_conv') # create a new command purge_conv that clears the channel
async def delete(ctx, amount: int = 100):
    await ctx.channel.purge(limit = amount + 1)

@client.command(name='shutdown') # create a new command shutdown that shuts down the bot
@commands.is_owner()
async def shutdown(ctx):
    """Shutdown the bot."""
    await client.close()

client.run(token)
