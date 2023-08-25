
def high_card(hand, table):                 #determines the high card using a given hand of cards, and the table cards
    unique_numbers = []
    for item in table:
        if(item.nums() not in unique_numbers):
            unique_numbers.append(item.nums())
    for item in hand:
        if(item.nums() not in unique_numbers):
            unique_numbers.append(item.nums())
    unique_numbers.sort()
    return unique_numbers[-1]/100          #The number isn't returned as itself, so as not to interfere with the other combinations that returns number points > 1

def max_of_a_kind(hand, table):         #returns how many of the same number cards there are
    dict = {}
    determining_factors = []            
    for item in table:
        if(item.nums() not in dict):
            dict[item.nums()] = 1
        else:
            dict[item.nums()] += 1
    for item in hand:
        if(item.nums() not in dict):
            dict[item.nums()] = 1
        else:
            dict[item.nums()] += 1

    key_values = []
    for item in dict:
        key_values.append(dict[item])
    key_values.sort()
    
    dict_values = sorted(dict.values())
    dict_sort_by_values = {}
    for value in dict_values:           #sorts the dictionary by value
        for item in dict:
            if(dict[item] == value):
                dict_sort_by_values[item] = value

    if(key_values[-1] != 1):                        
        if(key_values[-1] == 2 and key_values[-2] == 2):                #Determine if there are two sets of two of a kind
            determining_factors.append(3)                               #Point value for having two sets of two of a kind
            determining_factors.append(list(dict_sort_by_values)[-1])   #Number value of the higher set of two of a kind, used in case of a tie
            determining_factors.append(high_card(hand,table))           #The highest card the given hand in combination with the table, used in case of a tie
            return determining_factors
        elif(key_values[-1] == 2):                                      #Determines if there is one set of two of a kind
            determining_factors.append(2)                               #Point value for having one set of two of a kind
            determining_factors.append(list(dict_sort_by_values)[-1])   #Number value of the two of a kind, used in case of a tie
            determining_factors.append(high_card(hand,table))           #The highest card the given hand in combination with the table, used in case of a tie
            return determining_factors                              
        elif(key_values[-1] == 3):                                      #Determines if there is three of a kind
            determining_factors.append(4)                               #Point value for having three of a kind
            determining_factors.append(list(dict_sort_by_values)[-1])   #Number value of the three of a kind, used in case of a tie
            determining_factors.append(high_card(hand,table))           #The highest card the given hand in combination with the table, used in case of a tie
            return determining_factors
        elif(key_values[-1] == 4):                                      #Determines if there is four of a kind
            determining_factors.append(8)                               #Point value for having four of a kind
            determining_factors.append(list(dict_sort_by_values)[-1])   #Number value of the four of a kind, used in case of a tie
            determining_factors.append(high_card(hand,table))           #The highest card the given hand in combination with the table, used in case of a tie
            return determining_factors
    return [0]

def straight(hand, table):             #determines if a given hand, in combination with the table cards, consists of five consecutive numbers
    unique_numbers = []
    determining_factors = []
    for item in table:
        if(item.nums() not in unique_numbers):
            unique_numbers.append(item.nums())
    for item in hand:
        if(item.nums() not in unique_numbers):
            unique_numbers.append(item.nums())
    
    unique_numbers.sort()
    if(len(unique_numbers) >= 5):
        for i in range(len(unique_numbers) - 4):
                if((unique_numbers[i] + 4) == unique_numbers[i+4]):
                    determining_factors.append(5)                       #Point value for having five numbers in row
                    determining_factors.append(unique_numbers[i+4])     #Number value of the fifth consecutive number, used in case of a tie
                    determining_factors.append(high_card(hand,table))   #The highest card the given hand in combination with the table, used in case of a tie
                    return determining_factors
    return [0]

def flush(hand, table):               #determins if a given hand, in combination with the table cards, consists of five same suit cards
    dict = {}
    determining_factors = []
    for item in table:
        if(item.suits() not in dict):
            dict[item.suits()] = 1
        else:
            dict[item.suits()] += 1
    for item in hand:
        if(item.suits() not in dict):
            dict[item.suits()] = 1
        else:
            dict[item.suits()] += 1
    dict_keys = []
    for item in dict:
        dict_keys.append(dict[item])
    dict_keys.sort()
    if(int(dict_keys[-1]) >= 5):
        determining_factors.append(6)                       #Point value for having five of the same suit card
        determining_factors.append(high_card(hand, table))  ##The highest card the given hand in combination with the table, used in case of a tie
        return determining_factors
    return [0]

def full_house(hand, table):          #determines if the there is a set of three of the same number card, and a different set of two of the same number card
    dict = {}
    determining_factors = []
    for item in table:
        if(item.nums() not in dict):
            dict[item.nums()] = 1
        else:
            dict[item.nums()] += 1
    for item in hand:
        if(item.nums() not in dict):
            dict[item.nums()] = 1
        else:
            dict[item.nums()] += 1
    key_values = []
    for item in dict:
        key_values.append(dict[item])
    key_values.sort()
    if(key_values[-1] >= 3 and key_values[-2] >= 2):
        determining_factors.append(7)                       #Point value for having the full house combination
        determining_factors.append(key_values[-1])          #Number value of the higher number set, used in case of a tie
        determining_factors.append(high_card(hand,table))   #The highest card the given hand in combination with the table, used in case of a tie
        return determining_factors
    return [0]

def higher_level_flush(hand, table):   #determines if there is a straight, where the five consecutive number have the same suite
    unique_numbers = []
    numbers_used = []
    for item in table:
        if(item.nums() not in numbers_used):
            unique_numbers.append(item)
            numbers_used.append(item.nums())
    for item in hand:
        if(item.nums() not in numbers_used):
            unique_numbers.append(item)
            numbers_used.append(item.nums())
    
    unique_numbers.sort(key = lambda x: x.nums())     #Sorts all the cards according in ascending order, while keeping the items of the list as object locations
    suit = ""
    counter = 0
    for i in range(len(unique_numbers) - 4):
        if(unique_numbers[i].nums() + 4 == unique_numbers[i + 4].nums()): #Flush could be from 1-5 or 2-6, so go backwards to get the largest one
            suit = unique_numbers[i].suits()
            for j in range(i,(i+5)):
                if(unique_numbers[j].suits() == suit):
                    counter += 1
                else:
                    if(j+1 < len(unique_numbers)):
                        suit = unique_numbers[j+1].suits()
                    counter = 0
            if(counter >= 5 and unique_numbers[-1].nums() == 14):    #Checks for a Royal Flush, meaning  the consecuetive number cards go from 10 - Ace
                return 10       
            elif(counter >= 5):                                   #Checks for a Straight Flush, meaning all consecueitve cards with same suit, not from 10 - Ace
                return 9
    return 0
