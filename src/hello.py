import csv, statistics

def average_score(path="data/users.csv"):
    with open(path) as f:
        return statistics.mean(float(r["score"]) for r in csv.DictReader(f))

if __name__ == "__main__":
    print(f"Average user score: {average_score():.2f}")
