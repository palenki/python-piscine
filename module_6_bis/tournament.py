from ex3 import CreatureFactory, FlameFactory, TransformCreatureFactory
from ex4 import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    InvalidStrategyError,
)

Opponent = tuple[CreatureFactory, BattleStrategy]


def run_tournament(opponents: list[Opponent]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved\n")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            factory1, strategy1 = opponents[i]
            factory2, strategy2 = opponents[j]

            fighter1 = factory1.create_base()
            fighter2 = factory2.create_base()

            print("* Battle *")
            print(fighter1.describe())
            print("vs.")
            print(fighter2.describe())
            print("now fight!")

            try:
                actions1: list[str] = strategy1.act(fighter1)
                actions2: list[str] = strategy2.act(fighter2)
            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return

            for action in actions1:
                print(action)
            for action in actions2:
                print(action)


def main() -> None:
    flame_factory = FlameFactory()
    transform_factory = TransformCreatureFactory()

    normal_strategy = NormalStrategy()
    aggressive_strategy = AggressiveStrategy()

    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Shiftling+Aggressive) ]")
    run_tournament([
        (flame_factory, normal_strategy),
        (transform_factory, aggressive_strategy),
    ])

    print()

    print("Tournament 1 (error)")
    print("[ (Shiftling+Aggressive), (Flameling+Aggressive) ]")
    run_tournament([
        (transform_factory, aggressive_strategy),
        (flame_factory, aggressive_strategy),
    ])


if __name__ == "__main__":
    main()
