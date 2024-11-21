
import random

class Player:
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role

        self.level = 1


        self.strength = 10
        # self.locations = 'art room', 'principal\'s office', 'music room'

        self.assign_stats()

    def print_character_sheet(self):
        print('Name: ' + self.name)
        print('Role: ' + self.role)
        print('Level: ' + str(self.level))
        print('------')
        print('Strength: ' + str(self.strength))
        

    def assign_stats(self):
        stats = [10, 15, 20, 30]
        random.shuffle(stats)
        self.strength = stats[0]

    # def assign_stats(self):
    #     stats = ('art room', 'principle room', 'music room')

    
        
        