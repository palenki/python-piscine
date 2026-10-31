#! /usr/bin/env python3

import random
import typing


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = [
            "run",
            "eat",
            "sleep",
            "grab",
            "move",
            "climb",
            "swim",
            "release",
            "use",
        ]

    while True:
        player = random.choice(players)
        action = random.choice(actions)
        yield (player, action)


def consume_event(
            events_list: list[tuple[str, str]],
        ) -> typing.Generator[tuple[str, str], None, None]:
    while events_list:
        random_index: int = random.randrange(len(events_list))
        event: tuple[str, str] = events_list.pop(random_index)
        yield event


def main() -> None:
    print("=== Game Data Stream Processor ===")

    stream = gen_event()

    for i in range(1000):
        player, action = next(stream)
        print(f"Event {i}: Player {player} did action {action}")

    event_list: list[tuple[str, str]] = []
    for _ in range(10):
        event = next(stream)
        event_list.append(event)
    print(f"Built list of 10 events: {event_list}")

    for event in consume_event(event_list):
        print(f"Got event from list {event}")
        print(f"Remains in list: {event_list}")


if __name__ == "__main__":
    main()
