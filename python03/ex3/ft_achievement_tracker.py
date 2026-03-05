#!/usr/bin/env python3

def print_analytics(p1: set, p2: set, p3: set) -> None:
    print("\n=== Achievement Analytics ===")
    uniques = {'boss_slayer', 'collector', 'first_kill', 'level_10',
               'perfectionist', 'speed_demon', 'treasure_hunter'}
    print(f"All unique achievements: {uniques}")
    print(f"Total unique achievements: {len(uniques)}")
    common = p1 & p2 & p3
    print(f"\nCommon to all players: {common}")
    rare = (p1 - p2 - p3 | p2 - p3 - p1 | p3 - p2 - p1)
    print(f"Rare achievements (1 player): {rare}")
    print(f"\nAlice vs Bob common: {p1.intersection(p2)}")
    print(f"Alice unique: {p1.difference(p2)}")
    print(f"Bob unique: {p2 - p1}")


def track_achievements(p1: set, p2: set, p3: set) -> None:
    print("=== Achievement Tracker System ===")
    print(f"Player alice achievements: {p1}")
    print(f"Player bob achievements: {p2}")
    print(f"Player charlie achievements: {p3}")


def main() -> None:
    alice_achievements = {'first_kill', 'level_10', 'treasure_hunter',
                          'speed_demon'}
    bob_achievements = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie_achievements = {'level_10', 'treasure_hunter', 'boss_slayer',
                            'speed_demon', 'perfectionist'}
    track_achievements(alice_achievements, bob_achievements,
                       charlie_achievements)
    print_analytics(alice_achievements, bob_achievements, charlie_achievements)


if __name__ == "__main__":
    main()
