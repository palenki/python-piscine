import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        raw_input: str = input("Enter new coordinates"
                               " as floats in format 'x,y,z': ")
        parts: list[str] = raw_input.split(",")

        if len(parts) != 3:
            print("Invalid syntax")
            continue
        try:
            x: float = float(parts[0].strip())
            y: float = float(parts[1].strip())
            z: float = float(parts[2].strip())
            return (x, y, z)
        except ValueError:
            for part in parts:
                cleaned: str = part.strip()
                try:
                    float(cleaned)
                except ValueError:
                    print(f"Error on parameter '{cleaned}': "
                          f"could not convert string to float: '{cleaned}'")
                    break


def calculate_distance(pos1: tuple[float, float, float],
                       pos2: tuple[float, float, float] = (0.0, 0.0, 0.0)
                       ) -> float:
    x1, y1, z1 = pos1
    x2, y2, z2 = pos2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)


def main() -> None:
    print("=== Game Coordinate System ===\n"
          "Get a first set of coordinates")
    pos1: tuple[float, float, float] = get_player_pos()
    print(f"Got a first tuple: {pos1}\n"
          f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")
    dist_to_center: float = round(calculate_distance(pos1), 4)
    print(f"Distance to center: {dist_to_center}\n")

    print("Get a second set of coordinates")
    pos2 = get_player_pos()
    dist_between = round(calculate_distance(pos1, pos2), 4)
    print(f"Distance between the 2 sets of coordinates: {dist_between}")


if __name__ == "__main__":
    main()
