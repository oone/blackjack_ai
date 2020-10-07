# Pygame Template
# Use this to start a new Pygame project
# KidsCanCode 2015
import pygame
import random

# define some colors (R, G, B)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)       
FUCHSIA = (255, 0, 255)
GRAY = (128, 128, 128)
LIME = (0, 128, 0)
MAROON = (128, 0, 0)
NAVYBLUE = (0, 0, 128)
OLIVE = (128, 128, 0)
PURPLE = (128, 0, 128)
RED = (255, 0, 0)
SILVER = (192, 192, 192)
TEAL = (0, 128, 128)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
CYAN = (0, 255, 255)

# basic constants to set up your game
WIDTH = 360
HEIGHT = 480
FPS = 30
BGCOLOR = GREEN

# initialize pygame
pygame.init()
# initialize sound - uncomment if you're using sound
# pygame.mixer.init()
# create the game window and set the title
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
# start the clock
clock = pygame.time.Clock()

# set the 'running' variable to False to end the game
running = True


class playgame:
    def __init__(self, playgame):   
            self.playgame = playgame  

    def random_card_value(self):
        card_num = random.randint(0, 14)
        card_num = 7
        if card_num > 9 and card_num < 14:
            card_value = 10
        if card_num == 14:
            card_value = 1
        if card_num < 10:
            card_value = card_num
        return (card_value)

    #def show_card_value(self, card_num):

    def sim_dealer_hand(self): 
        card_1 = self.random_card_value()
        card_2  = self.random_card_value()
        card_total = card_1 + card_2
        while card_total < 17 and card_total <= 21:
            card_total += random_card_value()
        if card_total > 21: 
            return ("bust")
        return(card_total)
    
    def get_player_hand(self):
        card_1 = self.random_card_value()
        card_2  = self.random_card_value()
        card_total = card_1 + card_2
        while card_total < 17 and card_total <= 21:
            card_total += random_card_value()
        if card_total > 21: 
            return ("bust")
        return(card_total)

    dealer_hand = self.sim_dealer_hand()
    player_hand = self.get_player_hand()

    def check_who_wins(self, player_hand):
        if player_hand == "bust":
            return("lost")
        if dealer_hand == "bust":
            return("won")
        if dealer_hand == player_hand:
            return("tie")
        if player_hand > dealer_hand:
            return("won")
        if player_hand < dealer_hand:
            return("lost")
    
    def hit_hand_until(self, player_hand, When_to_stop):
        while card_total < When_to_stop and card_total <= 21:
            card_total += random_card_value()
        if card_total > 21: 
            return ("bust")
        return(card_total)

class bots:
    def __init__(self, bots):   
            self.bots = bots  

    starting_values = (0, 100)

    def generate_bots_first_stand_number(self):
            stand_number = random.randint(starting_values)
            return (stand_number)

    def gener

    
    def generate_bots_ending_hands(self, how_many_bots):
        while how_many_bots > 0:
            bot_name = how_many_bots
            how_many_bots = how_many_bots - 1
            dealer_hand = playgame.sim_dealer_hand()
            player_hand = playgame.get_player_hand()
            if 
            result = playgame.hit_hand_until(player_hand, )









        
        


# start the game loop
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        # add any other events here (keys, mouse, etc.)

    # Game loop part 2: Updates #####

    # Game loop part 3: Draw #####
    screen.fill(BGCOLOR)
    # after drawing, flip the display
    pygame.display.flip()

# close the window
pygame.quit()