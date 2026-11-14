from ex3 import CreatureFactory, FlameFactory, TransformCreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    base = factory.create_base()
    evolved = factory.create_evolved()

    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


def test_battle(factory1: CreatureFactory,
                factory2: CreatureFactory) -> None:
    print("Testing battle")
    fighter1 = factory1.create_base()
    fighter2 = factory2.create_base()

    print(fighter1.describe())
    print("vs.")
    print(fighter2.describe())
    print("fight!")
    print(fighter1.attack())
    print(fighter2.attack())


if __name__ == "__main__":
    flame_factory = FlameFactory()
    transform_factory = TransformCreatureFactory()

    test_factory(flame_factory)
    print()
    test_factory(transform_factory)
    print()
    test_battle(flame_factory, transform_factory)
