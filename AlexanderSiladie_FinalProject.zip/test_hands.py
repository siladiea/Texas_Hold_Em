import unittest
import hands

class Card:     #This is the Cards class from main.py. I tried importing it, but when I would run this file, the print statements from main.py would appear
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

class TestHands(unittest.TestCase):

    def test_one_pair(self):                    #This is the highest probable combination in Texas Hold Em, a one pair(two cards with the same number)
        list1 = []                              #similutaes a given hand(users or computers)
        list1.append(Card(NUMBERS[0],SUITS[1]))
        list1.append(Card(NUMBERS[0],SUITS[2]))
        list2 = []                               #similutes the cards on the table
        list2.append(Card(NUMBERS[10],SUITS[1]))
        list2.append(Card(NUMBERS[9],SUITS[0]))
        list2.append(Card(NUMBERS[3],SUITS[2]))
        list2.append(Card(NUMBERS[8],SUITS[1]))
        list2.append(Card(NUMBERS[6],SUITS[3]))

        same_num = hands.max_of_a_kind(list1, list2)        
        self.assertEqual(same_num[0], 2)           #test to see that the correct point value is given for having a one a pair

        list2.pop()
        list2.append(Card(NUMBERS[0],SUITS[3]))
        same_num = hands.max_of_a_kind(list1, list2)
        self.assertNotEqual(same_num[0], 2)     #if there are three cards with the same number(another combination), the point value for a one pair isn't assigned

    def test_two_pair(self):              #This is the 2nd highest probable combination in Texas Hold Em, a two pair(two sets of two cards with the same number)     
        list1 = []                          #similutaes a given hand(users or computers)
        list1.append(Card(NUMBERS[0],SUITS[1]))
        list1.append(Card(NUMBERS[0],SUITS[2]))
        list2 = []                                  #similutes the cards on the table
        list2.append(Card(NUMBERS[10],SUITS[1]))
        list2.append(Card(NUMBERS[9],SUITS[0]))
        list2.append(Card(NUMBERS[3],SUITS[2]))
        list2.append(Card(NUMBERS[8],SUITS[1]))
        list2.append(Card(NUMBERS[8],SUITS[3]))
        same_num = hands.max_of_a_kind(list1, list2)
        self.assertEqual(same_num[0], 3)                #test to see that the correct point value is given for having a two a pair

        list2.pop()
        list2.append(Card(NUMBERS[0],SUITS[3]))
        same_num = hands.max_of_a_kind(list1, list2)
        self.assertNotEqual(same_num[0], 2)     #if there are three cards with the same number, the point value for a two pair isn't assigned



if __name__ == '__main__':
    unittest.main()