import json

def loadData() -> dict:
    with open("data/movies.json") as f:
        data: dict = json.load(f)

        return data
