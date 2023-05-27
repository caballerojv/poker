import helpers
import cards


class Dealer:
    def __init__(self) -> None:
        pass

    def get_common_cards(self):
        return [self.deck.give_top_card() for _ in range(5)]

    def give_personal_cards(self):
        return [self.deck.give_top_card() for _ in range(2)]

    def __str__(self):
        return "".join(f"{card.value}{card.suit}" for card in self.cards_for_player)


class Player:
    def __init__(self) -> None:  # acabar player
        pass
