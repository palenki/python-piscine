#! /usr/bin/env python3
import sys


def main() -> None:
    print("=== Inventory System Analysis ===")

    inventory = {}

    for arg in sys.argv[1:]:
        if ":" not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue

        parts = arg.split(":", 1)
        name = parts[0]
        qty_str = parts[1]

        if name in inventory:
            print(f"Redundant item '{name}' - discarding")
            continue

        try:
            qty = int(qty_str)
            inventory[name] = qty
        except ValueError:
            print(f"Quantity error for '{name}':"
                  f" invalid literal for int() with base 10: '{qty_str}'")

    print(f"Got inventory: {inventory}")

    if len(inventory) == 0:
        print("At the beginning of the game, "
              "your inventory is usually empty ;)")
        return

    item_list: list[str] = list(inventory.keys())
    print(f"Item list: {item_list}")

    total_qty: int = sum(inventory.values())
    num_items: int = len(inventory)
    print(f"Total quantity of the {num_items} items: {total_qty}")

    if total_qty > 0:
        for name, qty in inventory.items():
            percentage: float = round((qty / total_qty) * 100, 1)
            print(f"Item {name} represents {percentage:.1f}%")

    most_item = None
    most_qty = None
    least_item = None
    least_qty = None

    for name, qty in inventory.items():
        if most_qty is None or qty > most_qty:
            most_qty = qty
            most_item = name

        if least_qty is None or qty < least_qty:
            least_qty = qty
            least_item = name
    print(f"Item most abundant: {most_item} with quantity {most_qty}")
    print(f"Item least abundant: {least_item} with quantity {least_qty}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
