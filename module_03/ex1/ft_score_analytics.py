import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    if len(sys.argv) < 2:
        print("No scores provided. "
              "Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return
    scores: list[int] = []
    for arg in sys.argv[1:]:
        try:
            score: int = int(arg)
            scores.append(score)
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    if len(scores) == 0:
        print("No scores provided. "
              "Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return
    total_players: int = len(scores)
    total_score: int = sum(scores)
    average_score: float = total_score / total_players
    high_score: int = max(scores)
    low_score: int = min(scores)
    score_range: int = high_score - low_score
    print(f"Scores processed: {scores}\n"
          f"Total players: {total_players}\n"
          f"Total score: {total_score}\n"
          f"Average score: {average_score}\n"
          f"High score: {high_score}\n"
          f"Low score: {low_score}\n"
          f"Score range: {score_range}\n")


if __name__ == "__main__":
    main()
