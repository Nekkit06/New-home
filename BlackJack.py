import cards, games

class BJ_Card(cards.Positionable_Card):
    ACE_VALUE = 1
    @property
    def value(self):
        if self.is_face_up:
            v = BJ_Card.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
        else:
            v = None
        return v



class BJ_Deck(cards.Deck):
    """ Black Jack Deck"""
    def populate(self):
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANKS:
                self.cards.append(BJ_Card(rank, suit))

    @property
    def total(self):
        for card in self.cards:
            if not card.value:
                return None

        t = 0
        contains_ace = False
        for card in self.cards:
            t += card.value
            if card.value == BJ_Card.ACE_VALUE:
                contains_ace = True
            
        if contains_ace and t <= 11:
            t += 10

        return t

        def is_busted(self):
            return self.total > 21



class BJ_Hand(cards.Hand):
    def __(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        rep = self.name + ":\t" + super().__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"
        return rep



class BJ_Player(BJ_Hand):
    def is_hitting(self):
        response = games.ask_yes_no("\n" + self.name + ", take more cards")
        return response == "y"

    def bust(self):
        print(self.name, "Took too much.")
        self.lose()

    def lose(self):
        print(self.name, " is defeated.")
    
    def win(self):
        print(self.name, " has won!")

    def push(self):
        print(self.name, " pushed.")



class BJ_Dealer(BJ_Hand):
    def is_hitting(self):
        return self.total < 17

    def bust(self):
        print(self.name, " took too much")

    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()


class BJ_Game:
    def __init__(self, names):
        self.players = []
        for name in names:
            player = BJ_Player(name)
            self.players.append(player)
        
        self.dealer = BJ_Dealer("Dealer")

        self.deck = BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()

    @property
    def still_playing(self):
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp

    def __additional_cards(self, player):
        while not player.is_busted() and player.is_hitting():
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                player.bust()

    def play(self):
        self.deck.deal(self.players + [self.dealer], per_hand = 2)
        self.dealer.flip_first_card()
        for player in self.players:
            print(player)
        print(self.dealer)

        for player in self.players:
            self.__additional_cards(player)
        self.dealer.flip_first_card()

        if not self.still_playing:
            print(self.dealer)
        else:
            print(self.dealer)
            self.__additional_cards(self.dealer)

            if self.dealer.is_busted():
                for player in self.still_playing:
                    player.win()
            else:
                for player in self.still_playing:
                    if player.total > self.dealer.total:
                        player.win()
                    elif player.total < self.dealer.total:
                        player.lose()
                    else:
                        player.push()

        for player in self.players:
            player.clear()
        self.dealer.clear()



def main():
    print("\t\tWelcome to Black Jack!\n")

    names = []
    number = games.ask_number("How many players in game?(1 - 7): ", low = 1, high = 7)

    for i in range(number):
        name = input("Enter player name ??? " + str(i + 1) + " :")
        names.append(name)
    print()

    game = BJ_Game(names)

    again = None
    while again != "n":
        game.play()
        again = games.ask_yes_no("\nWould you like to play again?")


main()



class BJ_Hand(cards.Hand):
    """BlackJack player hand"""
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        rep = self.name + ":\t" + super().__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"
        return rep  
        
#[c] Nekkit06
