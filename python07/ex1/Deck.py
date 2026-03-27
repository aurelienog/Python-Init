from ex0.Card import Card, CardType
from random import shuffle as shuf


class Deck():
    def __init__(self) -> None:
        self.cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        self.cards = [*self.cards, card]
        self.shuffle()

    def remove_card(self, card_name: str) -> bool:
        removed = False
        new_deck: list[Card] = []
        for card in self.cards:
            if not removed and card.name == card_name:
                removed = True
                continue
            else:
                new_deck = [*new_deck, card]
        if removed:
            self.shuffle()
            return True
        else:
            return False

    def shuffle(self) -> None:
        shuf(self.cards)

    def draw_card(self) -> Card:
        drawed = self.cards[0]
        self.cards = self.cards[1:]
        return drawed

    def get_deck_stats(self) -> dict[str, int | float]:
        sum_cost = 0
        creatures = 0
        spells = 0
        artifacts = 0
        sum_cost = 0
        total = 0

        for card in self.cards:
            total += 1
            match card.type:
                case CardType.CREATURE:
                    creatures += 1
                    sum_cost += card.cost
                case CardType.SPELL:
                    spells += 1
                    sum_cost += card.cost
                case CardType.ARTIFACT:
                    artifacts += 1
                    sum_cost += card.cost

        return {
            "total_cards": total,
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": sum_cost / total
        }
