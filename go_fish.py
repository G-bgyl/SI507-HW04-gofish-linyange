import random

deck = ['ace', 'ace', 'ace', 'ace', '2', '2', '2', '2', '3', '3', '3', '3', '4', '4', '4', '4', '5', '5', '5', '5', '6',
        '6', '6', '6', '7', '7', '7', '7', '8', '8', '8', '8', '9', '9', '9', '9', '10', '10', '10', '10', 'jack',
        'jack', 'jack', 'jack', 'queen', 'queen', 'queen', 'queen', 'king', 'king', 'king', 'king']

#initialize
my_hand = []
opponent_hand = []
my_score = 0
opponent_score = 0
exit = False
pointer={0:['Alice',my_hand,my_score],1:['Bob',opponent_hand,opponent_score]}
my_score = 0
opponent_score = 0

def draw(cards, owner,name,exit = False):
    if len(deck) >= cards:
        for i in range(0, cards):
            drawn_card = deck.pop((int)(random.random() * len(deck)))
            owner.append(drawn_card)
            if name=='Alice':
                print("Alice drew a %r." % drawn_card)
            else:
                print("Bob drew a %r." % drawn_card)
        if cards ==1:
            return (drawn_card,exit)
    else:
        print("No more cards in the deck.\n")
        if not my_hand and not opponent_hand:
            exit = True
    if name=='Alice':
        print("Alicia's hand:", my_hand,'\n')
    elif name=='Bob':
        print("Bob's hand:", opponent_hand,'\n')
    drawn_card=None
    # print(drawn_card, exit)
    re = (drawn_card, exit)
    return re


def check_hands(hand):
    i=0
    for each in hand[1]:  # checks hand for duplicates
        num = hand[1].count(each)
        if num == 4:
            i+=1
            print(hand[0], " have four of %rs! yay!" % each,'\n')

            for i in range(4):
                hand[1].remove(each)
            hand[2] += 1
            # print(hand)
            # print(hand[0], "'s current hand:", hand[1],'\n')
            return hand[2]
    if i ==0:
        # print(hand[0], 'didn\'t have same four cards for now, better luck next time!','\n')
        return hand[2]

def search_fish(giver,receiver,t):
    number = {0:'zero',1:'one',2:'two',3:'three',4:'four'}
    i=0
    for each in giver[1]:
        if each == t:
            i+=1
        # else:
        #     print(each,'not equal to',t )
    for j in range(i):
        giver[1].remove(t)
        receiver[1].append(t)
    print(giver[0],"gives ",receiver[0],number[i], t,'.\n')
    if i == 0 :
        print('Go fish!\n')
        drawn_card=draw(1,receiver[1],receiver[0])[0]
        if drawn_card != t:
            return False
        elif  drawn_card == t:
            return True
    elif i !=0:
        return True


def print_result(this_hand,other_hand):
    print(this_hand[0],"'s score:", this_hand[2])
    print(other_hand[0], "'s score:", other_hand[2])
    if this_hand[2] > other_hand[2]:
        print("Congratulations! {} won!".format(this_hand[0]))

    elif this_hand[2] < other_hand[2]:
        print("Congratulations! {} won!".format(other_hand[0]))

    elif this_hand[2] == other_hand[2]:
        print("You tied! Bummer!")

def start_game():
    print('Let\'s begin!')
    draw(7, my_hand,'Alice')
    draw(7, opponent_hand,'Bob')

    exit = False

    round=0
    while (not exit):

        this_hand = pointer[(round % 2)]
        other_hand =pointer[1-(round % 2)]
        this_hand[2] = check_hands(this_hand)
        other_hand[2] = check_hands(other_hand)

        iterate = True
        while iterate:

            t = input("%r, please choose a card from your hand to ask the opponent, or 'exit' to exit:\n" % this_hand[0])
            print('\n')
            t = t.lower()
            while t == 'exit' or t not in this_hand[1]:
                if t == "exit":
                    exit = True
                    print("You will now exit the game.",'\n')
                    break
                elif t not in this_hand[1] :
                    print("Sorry, you didn't choose a card from your hand.",'\n')
                    t = input( "%r ,please choose a card from your hand to ask the opponent, or 'exit' to exit:\n" % this_hand[0])
                    print('\n')
            if t == "exit":
                exit = True
                break

            if t in this_hand[1]:
                iterate = search_fish(other_hand,this_hand,t)
                this_hand[2] = check_hands(this_hand)

            if len(this_hand[1])==0:
                result = (0,'k')
                result = draw(1,this_hand[1],this_hand[0])
                exit=result[1]
            if len(other_hand[1])==0:
                result_1 = (0, 'k')
                result_1 = draw(1,other_hand[1],other_hand[0])
                exit = result_1[1]
            if len(this_hand[1])!=0 and len(other_hand[1])!=0:
                print('\n\nAlice:',my_hand,'\nBob:',opponent_hand,'\n\n')

            if exit==True:
                iterate=False
                break
        round +=1
    print_result(this_hand, other_hand)



start_game()

# search_fish([1,[0,1],1],[2,[1,2],0],3)
