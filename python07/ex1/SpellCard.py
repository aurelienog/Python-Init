from ex0.Card import Card, CardRarity, CardType


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: CardRarity) -> None:
        super().__init__(name, cost, rarity)
        self.type = CardType.SPELL