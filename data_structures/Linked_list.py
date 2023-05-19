from discord import Message
from data_structures.Node import Node
import json
import os

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

    def append(self, data):
        node = Node(data)
        if self.tail is None:
            self.head = node
            self.tail = node
            self.current = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            self.current = node

    def move_forward(self):
        if self.current is not None and self.current.next is not None:
            self.current = self.current.next

    def move_back(self):
        if self.current is not None and self.current.prev is not None:
            self.current = self.current.prev

    def clear(self):
        self.head = None
        self.tail = None
        self.current = None

    def get_last_command(self):
        if self.head is not None and self.head.next is None:
            return self.head.data
        if self.tail is not None:
            return self.tail.data

    def get_user_commands(self, user_id):
        commands = []
        node = self.head
        print(node.data)
        while node is not None:
            if node.data['author']['id'] == user_id:
                commands.append(node.data)
            node = node.next
        return commands

    def save_to_file(self, file_path):
        commands = []
        node = self.head
        while node is not None:
            commands.append(self.to_dict(node.data))
            node = node.next
        with open(file_path, 'w') as f:
            json.dump(commands, f)

    def load_from_file(self, file_path):
        if not os.path.exists(file_path):
            print("File does not exist.")
            return

        try:
            with open(file_path, 'r') as f:
                commands = json.load(f)
                for command_data in commands:
                    message_data = command_data
                    message = {}
                    message['id'] = message_data['id']
                    message['content'] = message_data['content']
                    message['channel'] = {
                        'type': message_data['channel']['type'],
                        'id': message_data['channel']['id'],
                        'name': message_data['channel']['name'],
                        'position': message_data['channel']['position'],
                        # 'nsfw': message_data['channel']['nsfw'],
                        # 'news': message_data['channel']['news'],
                        'category': message_data['channel']['category'],
                    }
                    message['type'] = message_data['type']
                    message['author'] = {
                        'id': message_data['author']['id'],
                        'name': message_data['author']['name'],
                        # 'discriminator': message_data['author']['discriminator'],
                        'bot': message_data['author']['bot'],
                        # 'nick': message_data['author']['nick'],
                        # 'guild': {
                        #     'id': message_data['author']['guild']['id'],
                        #     'name': message_data['author']['guild']['name'],
                        #     'shard_id': message_data['author']['guild']['shard_id'],
                        #     'chunked': message_data['author']['guild']['chunked'],
                        #     'member_count': message_data['author']['guild']['member_count'],
                        # },
                        # 'flags': message_data['author']['flags'],
                    }
                    self.append(message)
        except FileNotFoundError:
            print("File not found.")
    @staticmethod
    def to_dict(data):
        return {
                'content': data.content,
                'id': data.id,
                'channel': {
                    'type': data.channel.type.name,
                    'id': data.channel.id,
                    'name': data.channel.name,
                    'position': data.channel.position,
                    # 'nsfw': data.channel.nsfw,
                    # 'news': data.channel.is_news(),
                    'category': data.channel.category_id,
                },
                'type': data.type.name,
                'author': {
                    'id': data.author.id,
                    'name': data.author.name,
                    # 'discriminator': data.author.discriminator,
                    'bot': data.author.bot,
                    # 'nick': data.author.nick,
                    # 'guild': {
                    #     'id': data.author.guild.id,
                    #     'name': data.author.guild.name,
                    #     'shard_id': data.author.guild.shard_id,
                    #     'chunked': data.author.guild.chunked,
                    #     'member_count': data.author.guild.member_count,
                    # },
                    # 'flags': data.author.public_flags.value,
                },
        }
