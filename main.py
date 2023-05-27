import cards
import roles


class Game:
    def __init__(self, num_players):
        self.players = []
        for i in range(1, num_players + 1):
            player = roles.Player()
            player.name = f"Player {i}"
            self.players.append(player)
            # acabar main segun vayamos avanzando
        pass

    def start_game(self):
        self.dealer = roles.Dealer()
        self.deck = self.dealer.deck = cards.Deck()
        self.dealer.deck.shuffle_deck()
        self.dealer.get_common_cards()
        for player in self.players:
            player.cards = self.dealer.give_personal_cards()


game1 = Game(7)
print(game1.start_game())
print([player.name for player in game1.players])
