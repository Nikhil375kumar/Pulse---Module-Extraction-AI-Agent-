# extractor.py
from bs4 import BeautifulSoup
import requests

def extract_clean_content(url):
    try:
        res = requests.get(url)
        soup = BeautifulSoup(res.content, 'lxml')

        # Remove headers, nav, footer
        for tag in ['header', 'footer', 'nav', 'script', 'style']:
            for item in soup.find_all(tag):
                item.decompose()

        text_blocks = [tag.get_text(strip=True) for tag in soup.find_all(['h1', 'h2', 'h3', 'p', 'li']) if tag.get_text(strip=True)]
        return text_blocks
    except Exception as e:
        print(f"Failed to extract from {url}: {e}")
        return []


if __name__ == "__main__":
    url = "https://wordpress.org/documentation/"
    content = extract_clean_content(url)
    for line in content[:10]:  # print first 10 lines
        print(line)