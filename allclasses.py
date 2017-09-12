from settings import *

class Game(object):
    def __init__(self):
        pygame.init()
        gameDisplay = pygame.display.set_mode ((display_width,display_height))
        
        pygame.display.set_caption('RHSB')
        clock = pygame.time.Clock()


class Card(object):
    '''Base class for one card'''
    def __init__(self, name, mana, atk, hp):
        self.name = name
        self.mana = mana
        self.hp = int(hp)
        self.atk = atk
    def attack(self, enemy):
        enemy_hp = int(enemy.hp)
        enemy_hp -= int(self.atk)
        self.hp -= int(enemy.atk)
        enemy.hp =  enemy_hp
    def dead(self):
        if self.hp <=0:
            print ('\nКарта ',self.name, 'умерла')
            return True
    def __del__(self):
          pass
    def __str__(self):
 #       rep = '' ' mana = ' + str(self.mana)  + ' hp = ' + str(self.hp) + ' atk = ' + str(self.atk)
         rep = str(self.name) + ' atk = ' + str(self.atk) + ' hp = ' + str(self.hp) 
         return rep

class Player(object):
    '''Class for one player'''
    def __init__(self, name, mana, hand):
        self.name = name
        self.mana = mana
        self.hand = hand
    def __str__(self):
        rep = str(self.name)
    def dead(self):
        return len(hand) == 0

#class Deck(object):
