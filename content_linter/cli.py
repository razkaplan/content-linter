import argparse
from . import run


def main():
    parser = argparse.ArgumentParser(description="Lint markdown posts for SEO, keywords, and readability")
    parser.add_argument(
        "--posts-dir",
        default="_posts",
        help="Directory containing posts to lint",
    )
    parser.add_argument(
        "--keywords-file",
        default=".github/scripts/keywords.txt",
        help="Path to the keywords configuration file",
    )
    args = parser.parse_args()

    success = run(posts_dir=args.posts_dir, keywords_file=args.keywords_file)
    if not success:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
