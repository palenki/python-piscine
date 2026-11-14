from typing import cast
from ex3 import TransformCreatureFactory
from ex3.capability import TransformCapability


def main() -> None:
    print("Testing Creature with transform capability")
    factory = TransformCreatureFactory()

    base = factory.create_base()
    evolved = factory.create_evolved()

    print("base:")
    print(base.describe())
    print(base.attack())
    base_cap = cast(TransformCapability, base)
    print(base_cap.transform())
    print(base.attack())
    print(base_cap.revert())

    print()

    print("evolved:")
    print(evolved.describe())
    print(evolved.attack())
    evolved_cap = cast(TransformCapability, evolved)
    print(evolved_cap.transform())
    print(evolved.attack())
    print(evolved_cap.revert())


if __name__ == "__main__":
    main()
