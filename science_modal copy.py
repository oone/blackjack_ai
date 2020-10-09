import random


model = []
for i in range(0,12):
    model.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 , 0, 0, 0, 0])

def random_card_value():
    card_num = random.randint(1, 14)
    if card_num > 9 and card_num < 14:
        card_value = 10
    elif card_num == 14:
        card_value = 11
    elif card_num < 10:
        card_value = card_num
    return (card_value)

def sim_dealer_hand(): 
    card_1 = random_card_value()
    card_2  = random_card_value()
    card_total = card_1 + card_2
    while card_total < 17:
        card_total += random_card_value()
    if card_total > 21:
        card_total = 22
    return card_1, card_total

def get_player_hand():
    card_1 = random_card_value()
    card_2  = random_card_value()
    card_total = card_1 + card_2
    return(card_total)

def check_who_wins(player_hand, dealer_hand):
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

def hit_hand(card_total):
    card_total += random_card_value()
    return(card_total)
    

ticked = 0
generation = 1000000
while generation > 0:
    generation = generation - 1
    player_hand = get_player_hand()
    old_player_hand = player_hand
    dealer_hand = sim_dealer_hand()


    dealer_first_card = dealer_hand[0]
    dealer_total = dealer_hand[1]
    hit = True
    while player_hand <= 21 and hit:
        old_player_hand = player_hand
        if model[dealer_first_card][player_hand] <= 0: # Hit
            hit = True
            learning = -1
            player_hand = hit_hand(player_hand)
        else:
            hit = False
            learning = 1
        # print ("DEALER HAS [{}], SHOWING[{}], PLAYER_HAS [{}], HIT? [{}]".format(dealer_total, dealer_first_card, old_player_hand, hit))
        
        if hit:
            if player_hand < 21:  # No player Bust
                model[dealer_first_card][old_player_hand] = model[dealer_first_card][old_player_hand] + learning
            if player_hand > 21: # Player bust
                model[dealer_first_card][old_player_hand] = model[dealer_first_card][old_player_hand] - learning
        elif not hit:
            if  dealer_total > 21:  # Dealer Bust
                model[dealer_first_card][old_player_hand] = model[dealer_first_card][old_player_hand] + learning
            elif dealer_total > player_hand: # Player loses
                model[dealer_first_card][old_player_hand] = model[dealer_first_card][old_player_hand] - learning
            elif player_hand > dealer_total: # Player wins
                model[dealer_first_card][old_player_hand] = model[dealer_first_card][old_player_hand] + learning


for x in range(0,len(model)):
    for y in range(0, len(model[x])):
        if (x>0 and y>0):
            action = "STAND"
            if model[x][y] == 0:
                action =  "-"
            elif model[x][y] < 0:
                action = "HIT"

            if action != "-":
                print ("Dealer showing[{}], Player has[{}]: [{}]".format(x, y, action))
