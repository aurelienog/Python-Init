#!/usr/bin/env python3


def analyze(players: dict) -> None:
    print("\n=== Combined Analysis ===")
    total = len(players)
    print(f"Total players: {total}")
    achievements = {a for player in players
                    for a in players[player]["achievements"]}
    print(f"Total unique achievements: {len(achievements)}")
    average = (sum(sum(players[player]["scores"]) for player in players)
               / sum(len(players[player]["scores"]) for player in players))
    print(f"Average score: {average:.1f}")
    top = {
        "name": "",
        "points": 0,
        "achievements": []
    }
    for player in players:
        if sum(players[player]["scores"]) > top["points"]:
            top["name"] = player
            top["points"] = sum(players[player]["scores"])
            top["achievements"] = players[player]["achievements"]
    print(f'Top performer: {top["name"]} ({top["points"]} points,',
          f'{len(top["achievements"])} achievements)')


def print_set(players: dict) -> None:
    print("\n=== Set Comprehension Examples ===")
    players_list = {player for player in players}
    achievements = {a for player in players
                    for a in players[player]["achievements"]}
    regions = {players[player]["region"] for player in players}
    print(f"Unique players:{players_list}")
    print(f"Unique achievements: {achievements}")
    print(f"Active regions: {regions}")


def print_dict(players: dict) -> None:
    print("\n=== Dict Comprehension Examples ===")
    player_scores = {player: sum(players[player]["scores"])
                     for player in players}
    count = {player: len(players[player]["achievements"])
             for player in players}
    categories = {
        "high": 0,
        "medium": 0,
        "low": 0
    }
    for player in players:
        if max(players[player]["scores"]) > 4000:
            categories["high"] += 1
        elif max(players[player]["scores"]) >= 2000:
            categories["medium"] += 1
        else:
            categories["low"] += 1
    print(f"Player scores: {player_scores}")
    print(f"Score categories: {categories}")
    print(f"Achievement counts: {count}")


def print_list(players: dict) -> None:
    print("\n=== List Comprehension Examples ===")
    scorers = [p for p in players
               if max(players[p]["scores"]) > 2000]
    scores_doubled = [score * 2 for score in players["alice"]["scores"]]
    active = [key for key in players if players[key]["active"]]
    print(f"High scorers (>2000): {scorers}")
    print(f"Scores doubled: {scores_doubled}")
    print(f"Active players: {active}")


def main() -> None:
    players = {
        "alice": {
            "achievements": {'first_kill', 'level_10', 'treasure_hunter',
                             'speed_demon'},
            "scores": [1751, 4600, 2300, 842],
            "active": True,
            "region": "north"
        },
        "bob": {
            "achievements": {'first_kill', 'level_10', 'boss_slayer',
                             'collector'},
            "scores": [940, 1800, 1600, 1950],
            "active": True,
            "region": "east"
        },
        "charlie": {
            "achievements": {'level_10', 'treasure_hunter', 'boss_slayer',
                             'speed_demon', 'perfectionist'},
            "scores": [4300, 2150, 1800, 790],
            "active": True,
            "region": "central"
        },
        "diana": {
            "achievements": {'treasure_hunter', 'collector', 'speed_demon'},
            "scores": [750, 1150, 900, 2482],
            "active": False,
            "region": "central"
        }
    }
    print("=== Game Analytics Dashboard ===")
    print_list(players)
    print_dict(players)
    print_set(players)
    analyze(players)


if __name__ == "__main__":
    main()
