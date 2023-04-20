import discord # pip install discord.py
from discord.ext import commands
from data_structures import linked_list
import dotenv # pip install python-dotenv
import os

# Load the token from the .env file
dotenv.load_dotenv()
token = os.getenv('TOKEN')


intents = discord.Intents.all() # Enable all intents

client = commands.Bot(command_prefix = '!', intents = intents) # Create a bot

class extended_Linked(linked_list.linked_list):
	def __init__(self, first_data):
		super().__init__(first_data)
	def return_last(self):
		current_node = self.first_node
		while current_node.next_node != None:
			current_node = current_node.next_node
		return current_node.data

my_list = extended_Linked('first') # Create a linked list

@client.command(name='delete')
async def delete(ctx, amount: int = 50):
    await ctx.channel.purge(limit = amount + 1)
    my_list.append('delete')


@client.event
async def on_message(message):
    if message.content.lower().startswith('hello'):
        await message.channel.send('Hello!')
    await client.process_commands(message)


@client.command(name = 'history')
async def print_history(ctx):
    history = my_list.return_last()
    await ctx.send(f"Last 10 commands:\n{history}")

client.run(token)
