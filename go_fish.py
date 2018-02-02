import random

deck = ['ace', 'ace', 'ace', 'ace', '2', '2', '2', '2', '3', '3', '3', '3', '4', '4', '4', '4', '5', '5', '5', '5', '6',
        '6', '6', '6', '7', '7', '7', '7']
''', '8', '8', '8', '8', '9', '9', '9', '9', '10', '10', '10', '10', 'jack',
        'jack', 'jack', 'jack', 'queen', 'queen', 'queen', 'queen', 'king', 'king', 'king', 'king' '''
my_hand = []
opponent_hand = []
my_score = 0
opponent_score = 0
exit = False
pointer={0:['Alice',my_hand,my_score],1:['Bob',opponent_hand,opponent_score]}
my_score = 0
opponent_score = 0

def draw(cards, owner):
    if len(deck) >= cards:
        for i in range(0, cards):
            drawn_card = deck.pop((int)(random.random() * len(deck)))
            owner.append(drawn_card)
            if owner == my_hand:
                print("Alice drew a %r." % drawn_card)
            else:
                print("Bob drew a %r." % drawn_card)
        if cards ==1:
            return drawn_card
    else:
        print("No more cards in the deck.")
        if not my_hand and not opponent_hand:
            exit = True
    if owner == my_hand:
        print("Alicia's hand:", my_hand)
    elif owner ==opponent_hand:
        print("Bob's hand:", opponent_hand)

def check_hands(hand):
    i=0
    for each in hand[1]:  # checks hand for duplicates
        num = hand[1].count(each)
        if num == 4:
            i+=1
            print(hand[0], " have four of %rs! yay!" % each)

            for i in range(4):
                hand[1].remove(each)
            hand[2] += 1
            print(hand)
            print(hand[0], "'s current hand:", hand[1])
            return hand[2]
    if i ==0:
        print('better luck next time!')
        return hand[2]

def search_fish(giver,receiver,t):

        i=0
        for each in giver[1]:
            if each == t:
                i+=1
            # else:
            #     print(each,'not equal to',t )
        for j in range(i):
            giver[1].remove(t)
            receiver[1].append(t)
        print(giver[0],"gives ",receiver[0],i, t,'.')

        if i == 0 :
            print('Go fish!')
            drawn_card=draw(1,receiver[1])
            if drawn_card != t:
                return False
            elif  drawn_card == t:
                return True
        elif i !=0:
            return True


def print_result(my_score,opponent_score):
    print("Your score:", my_score)
    print("Your opponent's score:", opponent_score)
    if my_score > opponent_score:
        print("Congratulations! You won!")

    elif opponent_score > my_score:
        print("You suck! Your opponent won!")

    elif opponent_score == my_score:
        print("You tied! Bummer!")

def start_game():
    print('Let\'s begin!')
    draw(7, my_hand)
    draw(7, opponent_hand)

    exit = False

    round=0
    while (not exit):

        this_hand = pointer[(round % 2)]
        other_hand =pointer[1-(round % 2)]

        iterate = True
        while iterate:
            this_hand[2] = check_hands(this_hand)
            other_hand[2] = check_hands(other_hand)
            t = input("%r, please choose a card from your hand to ask the opponent, or 'exit' to exit:\n" % this_hand[0])
            t = t.lower()
            while t == 'exit' or t not in this_hand[1]:
                if t == "exit":
                    exit = True
                    print("You will now exit the game.")
                    break
                elif t not in this_hand[1] :
                    print("Sorry, you didn't choose a card from your hand.")
                    t = input( "%r ,please choose a card from your hand to ask the opponent, or 'exit' to exit:\n" % this_hand[0])

            if t == "exit":
                exit = True
                break

            if t in this_hand[1]:
                iterate = search_fish(other_hand,this_hand,t)
                this_hand[2] = check_hands(this_hand)

            if len(this_hand[1])==0:
                draw(1,this_hand)
            if len(other_hand[1])==0:
                draw(1,other_hand)
            print('\n\nAlice:',my_hand,'\nBob:',opponent_hand,'\n\n')
        round +=1
    print_result(my_score, opponent_score)



start_game()

