import os
import glob
import re
import requests
from bs4 import BeautifulSoup

def check_seo(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Check for title, description, and image
    if not re.search(r'^title: ".*"$', content, re.MULTILINE):
        print(f"Error: Missing title in {file_path}")
        return False
    if not re.search(r'^summary: ".*"$', content, re.MULTILINE):
        print(f"Error: Missing summary in {file_path}")
        return False
    if not re.search(r'!\[.*\]\(.*\)', content):
        print(f"Error: Missing image in {file_path}")
        return False

    # Check for broken links
    soup = BeautifulSoup(content, 'html.parser')
    links = [a['href'] for a in soup.find_all('a', href=True)]
    for link in links:
        if not link.startswith('http'):
            continue
        try:
            response = requests.head(link)
            if response.status_code >= 400:
                print(f"Error: Broken link {link} in {file_path}")
                return False
        except requests.RequestException:
            print(f"Error: Broken link {link} in {file_path}")
            return False

    return True

def check_keywords(file_path, keywords):
    with open(file_path, 'r') as file:
        content = file.read()

    for keyword in keywords:
        if keyword.lower() in content.lower():
            return True

    print(f"Error: None of the declared keywords found in {file_path}")
    return False

def main():
    keywords_file = '.github/scripts/keywords.txt'
    with open(keywords_file, 'r') as file:
        keywords = [line.strip() for line in file.readlines()]

    posts = glob.glob('_posts/**/*.markdown')
    for post in posts:
        if not check_seo(post):
            exit(1)
        if not check_keywords(post, keywords):
            exit(1)

if __name__ == "__main__":
    main()