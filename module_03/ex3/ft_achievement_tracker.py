#! /usr/bin/env python3
import random

ALL_ACHIEVEMENTS: set[str] = {
        'First Steps',
        'Master Explorer',
        'Boss Slayer',
        'Treasure Hunter',
        'Collector Supreme',
        'Crafting Genius',
        'Untouchable',
        'The Clever Mage',
        'World Savior',
        'Unstoppable',
        'Strategist',
        'Speed Runner',
        'Master Shaman',
        'Survivor',
        'Sharp Mind',
        'Hufflepuff Guy',
        'Hidden Path Finder'
}


def gen_player_achievements() -> set[str]:
    achievements_list: list[str] = list(ALL_ACHIEVEMENTS)
    count: int = random.randint(5, 9)
    selected: list[str] = random.sample(achievements_list, count)
    return set(selected)


def main() -> None:
    print("=== Achievement Tracker System ===\n")
    alice: set[str] = gen_player_achievements()
    bob: set[str] = gen_player_achievements()
    charlie: set[str] = gen_player_achievements()
    dylan: set[str] = gen_player_achievements()

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")

    players_achievements: set[str] = alice.union(bob, charlie, dylan)
    common_achievements: set[str] = alice.intersection(bob, charlie, dylan)
    print(f"\nAll distinct achievements: {players_achievements}\n\n"
          f"Common achievements: {common_achievements}\n")

    only_alice: set[str] = alice.difference(bob.union(charlie, dylan))
    only_bob: set[str] = bob.difference(alice.union(charlie, dylan))
    only_charlie: set[str] = charlie.difference(alice.union(bob, dylan))
    only_dylan: set[str] = dylan.difference(alice.union(bob, charlie))

    print(f"Only Alice has: {only_alice}\n"
          f"Only Bob has: {only_bob}\n"
          f"Only Charlie has: {only_charlie}\n"
          f"Only Dylan has: {only_dylan}\n")

    print(f"Alice is missing: {ALL_ACHIEVEMENTS.difference(alice)}\n"
          f"Bob is missing: {ALL_ACHIEVEMENTS.difference(bob)}\n"
          f"Charlie is missing: {ALL_ACHIEVEMENTS.difference(charlie)}\n"
          f"Dylan is missing: {ALL_ACHIEVEMENTS.difference(dylan)}")


if __name__ == "__main__":
    main()
