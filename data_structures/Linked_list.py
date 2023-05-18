from discord import Message
from data_structures.Node import Node
import json
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
        if self.tail is not None:
            return self.tail.data

    def get_user_commands(self, user_id):
        commands = []
        node = self.head
        while node is not None:
            if node.data.author.id == user_id:
                commands.append(node.data)
            node = node.next
        return commands

    def save_to_file(self, file_path):
        commands = []
        node = self.head
        while node is not None:
            commands.append(node.data.to_dict())
            node = node.next
        with open(file_path, 'w') as f:
            json.dump(commands, f)

    def load_from_file(self, file_path):
        try:
            with open(file_path, 'r') as f:
                commands = json.load(f)
        except FileNotFoundError:
            commands = []
        for command in commands:
            data = Message(**command)
            self.append(data)

