class BlackJack(object):
    def __init__(self):

        self.deck = [
            ('Ace of Clubs', 1),
            ('Two of Clubs', 2),
            ('Three of Clubs', 3),
            ('Four of Clubs', 4),
            ('Five of Clubs', 5),
            ('Six of Clubs', 6),
            ('Seven of Clubs', 7),
            ('Eight of Clubs', 8),
            ('Nine of Clubs', 9),
            ('Ten of Clubs', 10),
            ('Jack of Clubs', 10),
            ('Queen of Clubs', 10),
            ('King of Clubs', 10),
            ('Ace of Diamonds', 1),
            ('Two of Diamonds', 2),
            ('Three of Diamonds', 3),
            ('Four of Diamonds', 4),
            ('Five of Diamonds', 5),
            ('Six of Diamonds', 6),
            ('Seven of Diamonds', 7),
            ('Eight of Diamonds', 8),
            ('Nine of Diamonds', 9),
            ('Ten of Diamonds', 10),
            ('Jack of Diamonds', 10),
            ('Queen of Diamonds', 10),
            ('King of Diamonds', 10),
            ('Ace of Hearts', 1),
            ('Two of Hearts', 2),
            ('Three of Hearts', 3),
            ('Four of Hearts', 4),
            ('Five of Hearts', 5),
            ('Six of Hearts', 6),
            ('Seven of Hearts', 7),
            ('Eight of Hearts', 8),
            ('Nine of Hearts', 9),
            ('Ten of Hearts', 10),
            ('Jack of Hearts', 10),
            ('Queen of Hearts', 10),
            ('King of Hearts', 10),
            ('Ace of Spades', 1),
            ('Two of Spades', 2),
            ('Three of Spades', 3),
            ('Four of Spades', 4),
            ('Five of Spades', 5),
            ('Six of Spades', 6),
            ('Seven of Spades', 7),
            ('Eight of Spades', 8),
            ('Nine of Spades', 9),
            ('Ten of Spades', 10),
            ('Jack of Spades', 10),
            ('Queen of Spades', 10),
            ('King of Spades', 10)
        ]
        self.shuffledDeck = []

    def shuffle(self):
        import random
        self.shuffledDeck = random.sample(self.deck, len(self.deck))
        #print('shuffledDeck: ', self.shuffledDeck)

    def hit(self):
        return self.shuffledDeck.pop(0)


class Players(BlackJack):

    def __init__(self):
        super(Players, self).__init__()
        self.dealerHand = []
        self.playerHand = []
        self.playerCount = 0
        self.dealerCount = 0

    def showDealer(self):
        print("Dealer's hand:")
        for card in self.dealerHand[:-1]:
            print(card[0])
        print('Hidden')

    def showDealerAll(self):
        print("Dealer's hand:")
        for card in self.dealerHand:
            print(card[0])

    def printDeck(self):
        print(self.shuffledDeck)

    def showPlayer(self):
        print("Your hand:")
        for card in self.playerHand:
            print(card[0])

    def countPlayer(self):
        values = []
        for x in self.playerHand:
            if type(x[1]) == int:
                values.append(x[1])
        count = sum(values)
        self.playerCount = count

    def countDealer(self):
        values = []
        for x in self.dealerHand:
            if type(x[1]) == int:
                values.append(x[1])
        count = sum(values)
        self.dealerCount = count
    
def run():
    players = Players()

    # Shuffle and deal

    players.shuffle()
    players.playerHand.append(players.hit())
    players.playerHand.append(players.hit())
    players.showPlayer()
    players.dealerHand.append(players.hit())
    players.dealerHand.append(players.hit())
    players.showDealer()
    
    # Start the game

    turns = 0
    while True:
        players.countPlayer()
        players.countDealer()

        if players.playerCount == 21 and turns == 0:
            print('You got blackjack. You win.')
            break
        elif players.playerCount > 21:
            print('You went bust. Dealer wins.')
            break
        elif players.dealerCount > 21:
            print('Dealer went bust. You win.')
            break
        elif players.playerCount == 21:
            print('You got 21. You win.')
            break
        elif players.dealerCount == 21:
            print('The dealer got 21. Dealer wins.')
            break
        
        elif players.playerCount < 21:
            #players.showPlayer()
            playerTurn = False
            playerStand = False
            turn = input("It's your turn. Would you like to hit or stand? h/s")
            if turn.lower() == 'h':
                players.playerHand.append(players.hit())
                players.showPlayer()
                playerTurn = True
            elif turn.lower() == 's':
                playerTurn = True
                playerStand = True
        
        if playerTurn == True:
            if players.dealerCount < 17:
                print('Dealer takes a card.')
                players.dealerHand.append(players.hit())
                players.showDealer()
                turns += 1
                continue
            elif players.dealerCount >= 17:
                print('Dealer stands.')
                players.showDealer()
                #print(playerStand)
                if playerStand == True:
                    if players.playerCount > players.dealerCount:
                        print('You win.')
                        #players.showDealerAll()
                        break
                    elif players.playerCount < players.dealerCount:
                        print('Dealer wins.')
                        #players.showDealerAll()
                        break
                elif playerStand == False:
                    turns += 1
                    continue
run()
