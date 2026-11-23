import argparse

from lib.keyword_search import matchingTitles


def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    search_parser = subparsers.add_parser("search", help="Search movies using keywords")
    search_parser.add_argument("query", type=str, help="Search query")

    args = parser.parse_args()

    match args.command:
        case "search":
            print(f"Searching for: {args.query}")
            titles = matchingTitles(args.query)
            for i in range(1, 6):
                if i >= len(titles):
                    break
                print(f"{i}. {titles[i - 1]}")
        case _:
            parser.print_help()


if __name__ == "__main__":
    main()
