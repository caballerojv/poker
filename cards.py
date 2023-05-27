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
        return self.cards.pop(helpers.randint(0, len(self) - 1))

    def give_top_card(self) -> Card:
        return self.cards.pop()

    def give_down_card(self) -> Card:
        return self.cards.pop(0)

    def shuffle_deck(self):
        helpers.shuffle(self.cards)

    def show_random_card(self) -> Card:
        return self.cards[helpers.randint(0, Deck.TOTAL_CARDS - 1)]

    def show_top_card(self) -> Card:
        return self.cards[-1]
    
    def deal_hand(self):
        return [self.give_random_card() for _ in range(5)]
    
    def show_down_card(self) -> Card:
        return self.cards[0]

    def __len__(self):
        return len(self.cards)


class Hand:
    def __init__(self, hand) -> None:

        self.hand = hand 
        
    def get_values_hand(self):
        target = self.hand
        values_hand = []
        for key, _ in Card.GLYPHS.items():
           suit_cards = [(key, (card.value)) for card in target if card.suit == key]
           if suit_cards:
            values_hand.extend(suit_cards)
        return values_hand
              
              
    def get_combinations_values (self):
       
        values_hand = self.get_values_hand()
        suits, values = zip(*values_hand)
        poker_combinations = {
            "Royal Flush": 10, #"Escalera Real" #hecho
            "Straight Flush": 9, #"Escalera de Color"#hecho
            "Poker": 8, #hecho #"Poker"
            "Full House": 7, #hecho #"Full House"
            "Flush": 6, #"Color" #hecho
            "Straight": 5, #"Escalera"#hecho
            "Three of a Kind": 4, #hecho #"Trio"
            "Two Pair": 3, #hecho #"Dobles Parejas"
            "One Pair": 2, #hecho #"Pareja"
            "High Card": 1 #"Carta Alta" #hecho
        }
        
        value_counts = {}
        for value in values:
            value_counts[value] = value_counts.get(value, 0) + 1
        
        if 1 in value_counts.values() and list(value_counts.values()).count(2) == 2:
            return ("Two Pair", poker_combinations["Two Pair"])
        if 2 in value_counts.values() and list(value_counts.values()).count(1) == 3:   
            return ("One Pair", poker_combinations["One Pair"])                                     #aqui cojo y por las veces que salen con el count busco y comparo
        if 3 in value_counts.values() and list(value_counts.values()).count(2) == 1:
            return ("Full House", poker_combinations["Full House"])
        if 3 in value_counts.values() and list(value_counts.values()).count(1) == 2:
            return ("Three of a Kind", poker_combinations["Three of a Kind"])
        
        if list(value_counts.values()) == [1, 1, 1, 1, 1] :           
                values = sorted(values)
                consecutive = True
                if all(value == 1 for value in values):
                    return  ("Poker", poker_combinations["Poker"])
                for i in range(len(values)-1):
                    if values[i] +1 != values[i -1]:
                        consecutive = False
                if len(set(suits))== 1 :
                        return  ("Flush", poker_combinations["Flush"])
                if consecutive:   
                    if len(set(suits))== 1 :
                        if consecutive == False  and  values[0] == 1 and all(values[i] == i + 9 for i in range(1, len(values))):#esto usa all para comprobar si todos los elementos de values cumplen con la condicion de que sea del 10 al 13 y el primer valor es 1 por tanto escalera real
                            return  ("Royal Flush", poker_combinations["Royal Flush"])                                                                                                             
                        if consecutive: 
                            return  ("Straight Flush", poker_combinations["Straight Flush"]) 
                    else:
                        return    ("Straight", poker_combinations["Straight"]) 
                if not consecutive:
                   return("High Card", poker_combinations["High Card"])
       
     def get_max_value(self):
        values_hand = self.get_values_hand()
        _, values = zip(*values_hand)
        values = sorted(values)
        return max(values)

deck = Deck()
deck.shuffle_deck()
hand_cards = deck.deal_hand()
hand = Hand(hand_cards)
combination = hand.get_combinations_values()
values =  hand.get_values_hand()
print(combination)
print(values)
print(hand_cards)

#print(deck1.cards)
#print(deck1.give_random_card())
#print(deck1.give_top_card())
