import csv
from datetime import datetime
from constants import SCORE_FILE


def save_score(nickname, score, game_time):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    row = [timestamp, nickname, score, round(game_time,2)]
    with open(SCORE_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(row)


def load_scores():
    scores = []
    try:
        with open(SCORE_FILE, "r") as f:
            reader = csv.reader(f)

            for row in reader:
                timestamp, nickname, score, game_time = row
                scores.append((timestamp, nickname, int(score), float(game_time)))
    except FileNotFoundError:
        return []

    scores.sort(key=lambda x: x[2], reverse=True)

    return scores