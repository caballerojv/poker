import helpers
import cards


class Dealer:
    def __init__(self) -> None:
        table = []
        for _ in range(5):
            table.append(cards.Deck().give_top_card(self))
        self.table = table

        cards_for_player = []
        for _ in range(2):
            cards_for_player.append(cards.Deck().give_top_card(self))
        self.cards_for_player = cards_for_player


class Player:
    def __init__(self) -> None:
        pass


dealer1 = Dealer()
print(dealer1.cards_for_player)
print(dealer1.table)
