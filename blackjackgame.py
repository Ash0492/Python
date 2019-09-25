
import random

#defining global varibale for the card property
suits = ('Hearts','Diamonds', 'Spades','Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'King', 'Queen', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'King':10, 'Queen':10, 'Ace':11}

playing = True

# defining how a card should be
class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.rank + "of" + self.suit
#Now taking all the cards and making a deck of cards using list DS
class Deck:
    def __init__(self): 
        self.deck = [] #list of cards
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    def __str__(self): #dispalying the card composition in the deck
        deck_comp = ''
        deck_comp += '\n' + Card.__str__()
        return 'the deck has:- ' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck) #shuffling the cards

    def deal(self):
        single_card = self.deck.pop() #whenever the card is dealt or give to the delaer or player the card will be removed from the list
        return single_card

class hand:

    def __init__(self):
        self.card = []
        self.value = 0
        self.aces = 0

    def add_card(self,card):
        self.card.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces +=1

    def adjust_for_ace(self):
        if self.value > 21 and self.aces:
            self.value -=10
            self.aces +=1



class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total +=self.bet
    
    def lose_bet(self):
        self.total -= self.bet



#functions to play

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet?"))
        except ValueError:
            print("Please enter the value in the form of an integer:")
        else:
            if chips.bet>chips.total:
                print("Sorry your bet can't exceed" + chips.total)
            else:
                break

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing
    while True:
        x = input("Do you want to hit or stay? Enter h for hit and s for stay")
        if x[0].lower() == 'h':
            hit(deck,hand)
        elif x[0].lower() == 's':
            print("Player stay! Dealer begins to play")
            playing = False
        else:
            print("Sorry! Please try again!")
            continue
        break

def show_some(player,dealer):
    print("Dealer's hand")
    print("<Card Hidden>")
    print("\n" , dealer.card[1],sep = '\n' )
    print("player's hand:-", *player.card, sep = '\n')

def show_all(player,dealer):
    print("Dealer's hand : ", *dealer.card,sep = '\n')
    print("Value of the dealer's card" , dealer.value)
    print("player's hand: ", *player.card, sep = '\n')
    print("Vlaue of player's cards:", player.value)

def player_busts(player,dealer,chips):
    print("Player burts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer Busts!")
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print("Dealer Wins!")
    chips.lose_bet()


#play the game

while True:
    print("Welcome to blackjack! Go as far as 21 but not more. Aces count as 11 or 1")

    deck = Deck()
    deck.shuffle()

    #distribute the cards among the dealer and the player

    player_hand = hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    #setup player's chips

    player_chips = Chips()

    take_bet(player_chips)

    show_some(player_hand, dealer_hand)

    while playing:
        hit_or_stand(deck,player_hand)
        show_some(player_hand,dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand,player_chips)
            break

        if player_hand.value <=21:
            while dealer_hand.value < 17:
                hit(deck, dealer_hand)

        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value< player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        
        else:
            push(player_hand, dealer_hand)


        print("player's winnings stand at   " , player_chips.total)

        new_game = input("Do you want to play? y for yes and n for No")
        if new_game[0].lower() == 'y':
            playing = True
            continue
        else:
            print("Thanks for playing")
            break

