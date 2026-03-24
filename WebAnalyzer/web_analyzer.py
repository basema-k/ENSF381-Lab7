import requests
import re
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

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

    top5 = []

    for word in word_count:
        count = word_count[word]
    
        top5.append((word, count))
    
        top5.sort(key=lambda x: x[1], reverse=True)
    
        if len(top5) > 5:
            top5.pop()

    print("5 Most Frequent Words")
    for word, count in top5:
        print(f"{word}: {count}")

    # 5
    keyword = input("\nEnter a keyword to search: ").lower()
    text = soup.get_text().lower()
    count = text.count(keyword) 

    print(f"The word '{keyword}' appears {count} times.")

    # 6
    paragraphs = soup.find_all('p')

    longest_paragraph = ""
    max_words = 0

    for p in paragraphs:
        text = p.get_text().strip()
        words = text.split()
        
        # ignore short paragraphs
        if len(words) < 5:
            continue
        
        # check if this is the longest
        if len(words) > max_words:
            max_words = len(words)
            longest_paragraph = text

    print("Longest Paragraph")
    print(longest_paragraph)
    print(f"\nWord count: {max_words}")

    # 7
    labels = ['Headings', 'Links', 'Paragraphs']
    values = [headings_count, links_count, paragraphs_count]

    plt.bar(labels, values)
    plt.title('Deferred Work for Religious Holiday (No Group)') 
    plt.ylabel('Count')
    plt.savefig('web analysis results.png')
    plt.show()

except Exception as e:
    print(f"Error fetching content: {e}")

