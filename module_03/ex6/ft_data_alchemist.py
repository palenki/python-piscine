#! /usr/bin/env python3

import random


def main() -> None:
    print("=== Game Data Alchemist ===\n")

    players = ["Alice", "bob", "Charlie", "Liam",
               "dylan", "Emma", "Gregory", "john", "kevin", "PAULO"]

    print(f"Initial list of players: {players}")

    all_capitalized: list[str] = [name.capitalize() for name in players]
    print(f"New list with all names capitalized: {all_capitalized}")

    capitalized_only: list[str] = [name for name in players if name.istitle()]
    print(f"New list of capitalized names only: {capitalized_only}\n")

    random.seed(42)
    scores: dict[str, int] = {
            name: random.randint(50, 1000) for name in all_capitalized
    }
    print(f"Score dict: {scores}")

    avg_score: float = round(sum(scores.values()) / len(scores), 2)
    print(f"Score average is {avg_score}")

    high_score: dict[str, int] = {
            name: score for name, score in scores.items() if score > avg_score
    }
    print(f"High scores: {high_score}")


if __name__ == "__main__":
    main()
