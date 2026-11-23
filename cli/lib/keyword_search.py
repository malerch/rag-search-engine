from lib.search_utils import loadData


def matchingTitles(query: str) -> list[str]:
    results: list[str] = []
    for movie in loadData()["movies"]:
        if query in movie["title"]:
            results.append(movie["title"])

    return results
