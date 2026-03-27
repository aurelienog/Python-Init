from ex0.Card import Card, CardRarity, CardType


class ArtifactCard(Card):
    def __init__(self, name: str,
                 cost: int, rarity: CardRarity,
                 durability: int, effect: str) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity
        self.durability = durability
        self.effect = effect
        self.type = CardType.ARTIFACT

    def play(self, game_state: dict) -> dict:
        game_state["player"]["mana"] -= self.cost
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect
        }

    def activate_ability(self) -> dict:
        return {

        }