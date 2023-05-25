import helpers


class Card:
    SUITS = "♣◆❤♠"
    GLYPHS = {
        "♣": ("🃑🃒🃓🃔🃕🃖🃗🃘🃙🃚🃛🃝🃞"),
        "◆": ("🃁🃂🃃🃄🃅🃆🃇🃈🃉🃊🃋🃍🃎"),
        "❤": ("🂱🂲🂳🂴🂵🂶🂷🂸🂹🂺🂻🂽🂾"),
        "♠": ("🂡🂢🂣🂤🂥🂦🂧🂨🂩🂪🂫🂭🂮"),
    }

    def __init__(self, value: int, suit: str):
        self.value = value
        self.suit = suit

    def cmp_value(self) -> int:
        if self.value == 1:
            self.value = 14
        return self.value

    def __repr__(self):
        """Devuelve el glifo de la carta"""
        return Card.GLYPHS[self.suit][self.value - 1]


class Deck:
    TOTAL_CARDS = 52
    CARDS = list("".join([glyph for glyph in Card.GLYPHS.values()]))

    def __init__(self):
        self.cards = []
        for suit in Card.GLYPHS.keys():
            for num in range(1, 13 + 1):
                self.cards.append(Card(num, suit))

    def give_random_card(self) -> str:
        return self.cards.pop(helpers.randint(0, Deck.TOTAL_CARDS - 1))

    def give_top_card(self) -> str:
        return self.cards.pop(-1)

    def give_down_card(self) -> str:
        return self.cards.pop(0)

    def shuffle_deck(self):
        helpers.shuffle(self.cards)

    def show_random_card(self) -> str:
        return self.cards[helpers.randint(0, Deck.TOTAL_CARDS - 1)]

    def show_top_card(self) -> str:
        return self.cards[-1]

    def show_down_card(self) -> str:
        return self.cards[0]


class Hand:
    def __init__(self) -> None:
        pass

    def __str__(self):
        return

    def repeat_cards(self):
        pass


# deck1 = Deck()
# print(deck1.cards)
# deck1.shuffle_deck()
# print(deck1.cards)
# print(deck1.give_random_card())
# print(deck1.give_top_card())
