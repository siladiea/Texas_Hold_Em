import random
import hands 

class Card:             
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit
    
    def nums(self):
        return int(self.number)

    def suits(self):
        return self.suit

    def format_nicely(self):
        if(self.number == '11'):
            return f"Jack of {self.suit}"
        elif(self.number == '12'):
            return f"Queen of {self.suit}"
        elif(self.number == '13'):
            return f"King of {self.suit}"
        elif(self.number == '14'):
            return f"Ace of {self.suit}"
        return f"{self.number} of {self.suit}"

NUMBERS = ["2","3","4","5","6","7","8","9","10","11","12","13", "14"]
SUITS = ["Clubs", "Spades", "Diamonds", "Hearts"]

USER_MONEY = 1000
POT = 0

ROUND = 1

def choose_one_card(num, suit):                 #Chooses a random card
    return Card(num[random.randint(0, 12)], suit[random.randint(0, 3)])

def giving_one_card(num, suit, used , func):    #Returns that randomly selected card, and makes sure it's not already in use 
    card = func(num, suit)
    in_list = False
    used = [item for sublist in used for item in sublist] #Transforms used from a nested list, into a 1D list
    new_used = []
    for item in used:
        new_used.append(item.format_nicely())
    if(card.format_nicely() in new_used):               #Checks to make sure the card isn't already in place
        in_list = True
    while(in_list):                                     #Keeps drawing a card until it isn't already in use
        card2 = func(num, suit)
        if(card2.format_nicely() not in new_used):
            return card2
    return card

def distribute(nums, suit, burn, used, round, func1, func2 = giving_one_card):
    final_list = [[],[],[]]
    if(round == 1):
        for i in range(2):
            final_list[0].append(func2(nums, suit, used, func1))     #First item in final_list is the USER_HAND
            final_list[2].append(final_list[0][-1])                  
            final_list[1].append(func2(nums, suit, used, func1))     #Second item in final_list is the COMPUTER_HAND
            final_list[2].append(final_list[1][-1])                  #Third item in final_list is the CARDS_USED
        return final_list

    elif(round == 2):
        final_list[0].append(func2(nums, suit, used, func1))         #First item is the burned cards
        final_list[2].append(final_list[0][-1]) 
        for i in range(3):
            final_list[1].append(func2(nums, suit, used, func1))     #Second item in final_list is the TABLE_CARDS
            final_list[2].append(final_list[1][-1])                  #Third item in final_list is the CARDS_USED
        return final_list

    final_list[0].append(func2(nums, suit, used, func1))         #First item  in final_list is the BURNED_CARDS
    final_list[2].append(final_list[0][-1]) 
    final_list[1].append(func2(nums, suit, used, func1))        #Second item in final_list is the TABLE_CARDS
    final_list[2].append(final_list[1][-1])                     #Third item in final_list is the CARDS_USED
    return final_list

def reformat(cards):          #Changes from object location, to a readable card
    for item in cards:
        print(item.format_nicely())

def run_through_hands(hand, table):                                 #runs through all functions in hands.py, returning a list that determines outcome of each game
    hand_points = 0
    if(hands.higher_level_flush(hand, table) > hand_points):        #determines if a combination of the given hand and the table cards has a high scoring flush
        hand_points = [hands.higher_level_flush(hand, table)]
    elif(hands.full_house(hand, table)[0] > hand_points):           #determines if a combination of the given hand and the table cards has a full house
        hand_points = hands.full_house(hand, table)
    elif(hands.flush(hand, table)[0] > hand_points):                #determines if a combination of the given hand and the table cards has a flush
        hand_points = hands.flush(hand, table)
    elif(hands.straight(hand, table)[0] > hand_points):             #determines if a combination of the given hand and the table cards has a straight
        hand_points = hands.straight(hand, table)
    elif(hands.max_of_a_kind(hand, table)[0] > hand_points):        #determines if a combination of the given hand and the table cards has 2,3, or 4 of a kind
        hand_points = hands.max_of_a_kind(hand, table)
    elif(hands.high_card(hand, table) > hand_points):
        hand_points = [hands.high_card(hand, table)]                #determines the highest card in a given hand and the table cards
    return hand_points

def determine_winner(user, computer, table):                    #uses run_through_hands() results to determine if the user of computer has a stronger combination
    user_points = run_through_hands(user,table)
    computer_points = run_through_hands(computer, table)
    if(user_points[0] == computer_points[0]):
        return if_tie(user_points, computer_points)
    elif(user_points[0] > computer_points[0]):
        return "You Win"
    return "You Lose"

def if_tie(user, computer):                 #if the user and the computer have the same combination, other features are used to determined a win, lose or tie
    if(user[0] != computer[0]):
        if(user[0] > computer[0]):
            return "You Win"
        return "You Lose"
    if(len(user) > 0):
        if(user[1] != computer[1]):
            if(user[1] > computer[1]):
                return "You Win"
            return "You Lose"
    if(len(user) > 1):
        if(user[2] > computer[2]):
            return "You Win"
    return "You Lose"

def new_round():                                #Every new round it tells the user the important information, and draws the table cards
        print("A card has beeen burned")
        print("")
        user = [item for sublist in USER_HAND for item in sublist]
        table = [item for sublist in TABLE_CARDS for item in sublist]
        print("Your Cards: ")
        reformat(user)
        print("")
        print(f"You have ${USER_MONEY}")
        print("")
        print(f"The pot is ${POT}")
        print("")

        if(ROUND == 2):
            print("The Flop: ")
        elif(ROUND == 3):
            print("The Turn:")
        else:
            print("The River: ")
        reformat(table)

def check_amount(amt):                  #Check to see if the amonut entered is an integer
    try:
        int(amt)

    except:
        print("Please enter a whole number")
        while(type(amt) != int):
            amt = input("How much would you like to raise by: ")
            try:
                int(amt)
                break
            except:
                print("Please enter a whole number")
    return amt

def raise_or_check():                   #Asks the user if they want to raise the pot, or whether they want to continue with the game(known as 'check' in Poker)
    global USER_MONEY
    global POT
    RAISE_OR_CHECK = input("Would you like to raise or check: ")
    while(RAISE_OR_CHECK.upper() != "RAISE" and RAISE_OR_CHECK.upper() != "CHECK"):
        print("Please enter raise of check: ")
        RAISE_OR_CHECK = input("Would you like to raise or check: ")

    if(RAISE_OR_CHECK.upper() == "RAISE"):
        amt = input("How much would you like to raise by: ")
        amt = check_amount(amt)                                            #Used to ensure that if the user does raise, the raise is an integer

        amt = int(amt)
        while(int(amt) > USER_MONEY):                          #Ensures the raise is within the user's amount                                                                ################FIX THIS AND add coments to hands.py and add a second test case###############################
            print("Sorry that is more than you have")
            amt = input("How much would you like to raise by: ")
            amt = check_amount(amt)



        POT += (2 * int(amt))            #2* because the computer always matches the raise
        USER_MONEY -= int(amt)

def adding_table_cards():           #This function adds 'x' amount of cards to the table based on what round it is
    global ROUND

    print("")       #adding spacing to make the game more readable
    print("")

    CARDS = distribute(NUMBERS, SUITS, BURNED_CARDS, CARDS_USED, ROUND, choose_one_card) 
    TABLE_CARDS.append(CARDS[1])
    CARDS_USED.append(CARDS[2])
    new_round()
    raise_or_check()
    ROUND += 1

for i in range(5):          #Adds legibility for the user
    print("")

print("Hello! This is a recreation of the popular game Texas Hold Em")
print("You will be playing against the computer, and will have a starting amount of $1000")
play = input("Would you like to play: ")

while(play.upper() != "YES" and play.upper() != "NO"):          
    print("Plese enter yes or no")
    play = input("Would you like to play: ")

while(USER_MONEY > 50 and play.upper() == "YES"):       #plays the game as long as the user wants to, and has the money
    for i in range(7):
        print("")
    USER_HAND = []
    COMPUTER_HAND = []
    BURNED_CARDS = []
    CARDS_USED = []
    TABLE_CARDS = []

    PLAY = distribute(NUMBERS, SUITS, BURNED_CARDS, CARDS_USED, ROUND, choose_one_card)         #distributes the user and the computer their cards
    USER_HAND.append(PLAY[0])   
    COMPUTER_HAND.append(PLAY[1])  
    CARDS_USED.append(PLAY[2])
    x = [item for sublist in USER_HAND for item in sublist]
    print('Your cards are: ')
    reformat(x)
    print("")
    wants_to_play = input("The minimum to enter is 50$. Would you like to play: ")         
    while (wants_to_play.upper() != "YES" and wants_to_play.upper() != "NO"):       
        print("Please answer as yes or no")
        wants_to_play = input("The minimum to enter is 50$. Would you like to play: ")
    if(wants_to_play.upper() == "YES"):
        POT += 100
        USER_MONEY -= 50
        ROUND += 1

        adding_table_cards()

        for i in range(2):
            adding_table_cards()

        if ROUND == 5:
            user = [item for sublist in USER_HAND for item in sublist]
            computer = [item for sublist in COMPUTER_HAND for item in sublist]
            table = [item for sublist in TABLE_CARDS for item in sublist]
            game_result = determine_winner(user, computer, table)
            print(game_result)
            if(game_result == "You Win"):
                USER_MONEY += POT
            elif(game_result == "Tie"):
                USER_MONEY += POT/2
            POT = 0
            ROUND = 1
            print("")
        
        play = input("Would you like to play another round: ")
        while(play.upper() != "YES" and play.upper() != "NO"):
            print("Plese enter yes or no")
            play = input("Would you like to continue playing: ")

    else:
        user_response = input("Would you like a new hand: ")
        while(user_response.upper() != "YES" and user_response.upper() != "NO"):
            print("Please answer as yes or no")
            wants_to_play = input("Would you like a new hand: ")
        if(user_response.upper() == "YES"):
            pass
        else:
            break

if(USER_MONEY < 50):
   print("Sorry, you don't have enough money to continue playing")
