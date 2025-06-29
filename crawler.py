# crawler.py
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def is_valid_url(url):
    try:
        parsed = urlparse(url)
        return parsed.scheme in ('http', 'https')
    except:
        return False

def get_internal_links(base_url, max_depth=1):
    visited = set()
    to_visit = [(base_url, 0)]
    internal_links = []

    while to_visit:
        current_url, depth = to_visit.pop()
        if current_url in visited or depth > max_depth:
            continue
        try:
            response = requests.get(current_url)
            soup = BeautifulSoup(response.content, 'lxml')
            visited.add(current_url)
            internal_links.append(current_url)
            for link in soup.find_all('a', href=True):
                full_url = urljoin(current_url, link['href'])
                if base_url in full_url and full_url not in visited:
                    to_visit.append((full_url, depth + 1))
        except:
            continue
    return internal_links


# crawler.py (add this at the bottom)
if __name__ == "__main__":
    test_url = "https://wordpress.org/documentation/"
    print(f"Checking: {test_url}")
    if is_valid_url(test_url):
        links = get_internal_links(test_url, max_depth=1)
        print(f"\nTotal internal links found: {len(links)}")
        for link in links:
            print(link)
    else:
        print("Invalid URL")

