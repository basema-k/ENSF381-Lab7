import requests
from bs4 import BeautifulSoup
import re

url = "https://en.wikipedia.org/wiki/University_of_Calgary"

headers = {
    "User-Agent": "lab07-web-analyzer"
}
try:
    response = requests.get(url, headers=headers)
    response.raise_for_status() # Ensures the request was successful
    soup = BeautifulSoup(response.text, 'html.parser')
    print(f"Successfully fetched content from {url}")

    # print(soup.prettify())

    # 3
    headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    headings_count = len(headings)

    links = soup.find_all('a')
    links_count = len(links)

    paragraphs = soup.find_all('p')
    paragraphs_count = len(paragraphs)

    # print results
    print("Most Common HTML tags")
    print(f"Headings: {headings_count}")
    print(f"Links: {links_count}")
    print(f"Paragraphs: {paragraphs_count}")

    # 4
    text = soup.get_text()
    text = text.lower()
    words = re.findall(r'\b\w+\b', text)

    word_count = {} # empty dictionary

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

    # print
    print("Most Frequent Words")
    for word, count in sorted_words[:5]:
        print(f"{word}: {count}")

    # 5

    # 6

    # 7

except Exception as e:
    print(f"Error fetching content: {e}")

