import os
import glob
import re
import requests
from bs4 import BeautifulSoup
from spellchecker import SpellChecker
from textstat import flesch_reading_ease


def check_seo(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    errors = []

    title_match = re.search(r'^title: "(.*?)"$', content, re.MULTILINE)
    slug_match = re.search(r'^slug: "(.*?)"$', content, re.MULTILINE)
    description_match = re.search(r'^description: "(.*?)"$', content, re.MULTILINE)

    title = title_match.group(1) if title_match else "UNKNOWN"
    slug = slug_match.group(1) if slug_match else title.lower().replace(' ', '-')
    description = description_match.group(1).strip() if description_match else ""

    if not title_match:
        errors.append("Missing title")
    if not description:
        errors.append("Missing description")

    if errors:
        for error in errors:
            print(f"::error file={file_path}::{error}")
        return False, title, slug, description

    print(f"::notice file={file_path}::Blog Detected: {title} ({slug}) - Description: {description}")
    return True, title, slug, description


def check_keywords(file_path, keywords):
    with open(file_path, 'r') as file:
        content = file.read()

    found_keywords = [kw for kw in keywords if kw.lower() in content.lower()]

    if found_keywords:
        print(f"::notice file={file_path}::Keywords found: {', '.join(found_keywords)}")
        return True
    else:
        print(f"::error file={file_path}::No relevant keywords found")
        return False


def check_links(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    soup = BeautifulSoup(content, 'html.parser')
    links = [a['href'] for a in soup.find_all('a', href=True)]
    errors = []
    internal_links = 0
    external_links = 0

    for link in links:
        if link.startswith('http'):
            external_links += 1
            try:
                response = requests.head(link, allow_redirects=True)
                if response.status_code >= 400:
                    errors.append(f"Broken link: {link}")
            except requests.RequestException:
                errors.append(f"Broken link: {link}")
        else:
            internal_links += 1

    if errors:
        for error in errors:
            print(f"::error file={file_path}::{error}")
        return False

    if internal_links < 1:
        print(f"::warning file={file_path}::Not enough internal links (found {internal_links})")
    if external_links < 1:
        print(f"::warning file={file_path}::Not enough external links (found {external_links})")

    print(f"::notice file={file_path}::All links are valid")
    return True


def check_headings(file_path, title):
    with open(file_path, 'r') as file:
        content = file.read()

    headings = re.findall(r'(?m)^#+\s+', content)

    if not headings and not title:
        print(f"::error file={file_path}::No headings found")
        return False

    if not re.search(r'(?m)^#\s+', content) and not title:
        print(f"::error file={file_path}::Missing H1 heading")
        return False

    print(f"::notice file={file_path}::Headings structure OK")
    return True


def check_images(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    soup = BeautifulSoup(content, 'html.parser')
    images = soup.find_all('img')
    missing_alt = [img['src'] for img in images if not img.get('alt')]

    if missing_alt:
        for img in missing_alt:
            print(f"::error file={file_path}::Image missing alt text: {img}")
        return False

    if len(images) < 1:
        print(f"::warning file={file_path}::Not enough images (found {len(images)})")

    print(f"::notice file={file_path}::All images have alt text")
    return True


def check_spelling(file_path):
    with open(file_path, 'r') as file:
        content = file.read().lower()

    spell = SpellChecker()
    words = content.split()
    misspelled = spell.unknown(words)

    if misspelled:
        for word in misspelled:
            suggestion = spell.correction(word)
            if suggestion and suggestion != word:
                print(
                    f"::warning file={file_path}::Possible misspelled word '{word}'; did you mean '{suggestion}'?"
                )
            else:
                alternatives = spell.candidates(word) - {word}
                if alternatives:
                    print(
                        f"::warning file={file_path}::Possible misspelled word '{word}'; suggestions: {', '.join(sorted(alternatives))}"
                    )
                else:
                    print(f"::warning file={file_path}::Possible misspelled word: '{word}'")
        return False

    print(f"::notice file={file_path}::No spelling mistakes detected")
    return True


def check_readability(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    score = flesch_reading_ease(content)

    if score < 50:
        print(f"::warning file={file_path}::Low readability score: {score} (Try simplifying the content)")
        return False

    print(f"::notice file={file_path}::Readability score: {score}")
    return True


def run(posts_dir="_posts", keywords_file=".github/scripts/keywords.txt"):
    print("Running content linter...")

    with open(keywords_file, 'r') as file:
        keywords = [line.strip() for line in file.readlines()]

    pattern_md = os.path.join(posts_dir, '*.md')
    pattern_markdown = os.path.join(posts_dir, '*.markdown')
    posts = glob.glob(pattern_markdown) + glob.glob(pattern_md)
    print("Detected posts:", posts)

    if not posts:
        print("::error::No blog posts found in the _posts directory.")
        return False

    overall_success = True

    for post in posts:
        print(f"::group::Checking {post}")

        seo_ok, title, slug, description = check_seo(post)
        keywords_ok = check_keywords(post, keywords)
        links_ok = check_links(post)
        headings_ok = check_headings(post, title)
        images_ok = check_images(post)
        spelling_ok = check_spelling(post)
        readability_ok = check_readability(post)

        print(f"::group::Results for {title} ({slug})")
        print(f"SEO: {seo_ok}")
        print(f"Description: {'present' if description else 'missing'}")
        print(f"Keywords: {keywords_ok}")
        print(f"Links: {links_ok}")
        print(f"Headings: {headings_ok}")
        print(f"Images: {images_ok}")
        print(f"Spelling: {spelling_ok}")
        print(f"Readability: {readability_ok}")
        print("::endgroup::")

        if not all(
            [
                seo_ok,
                keywords_ok,
                links_ok,
                headings_ok,
                images_ok,
                spelling_ok,
                readability_ok,
            ]
        ):
            overall_success = False
            print(f"::error::Some checks failed for {post}")

        print(f"::endgroup::")

    return overall_success
