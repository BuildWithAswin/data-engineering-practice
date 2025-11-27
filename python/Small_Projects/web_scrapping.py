import requests
from bs4 import BeautifulSoup


def fetch_headlines():
    url = "https://feeds.bbci.co.uk/news/rss.xml"
    response = requests.get(url)
    print(response.text[:1000])  # print first 1000 chars of HTML

    if response.status_code != 200:
        print(f"failed to fetch page. Status code: {response.status_code}")
        return

    soup = BeautifulSoup(response.content, "xml")
    headlines = soup.find_all("item")

    print("\n Latest BBC headlines: \n")
    for i, headline in enumerate(headlines[:10], start=1):
        print(f"{i}. {headline.title.text}")


fetch_headlines()
