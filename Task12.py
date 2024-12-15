import requests
from bs4 import BeautifulSoup

def fetch_headlines(url, headline_tag, headline_class=None):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        
        if headline_class:
            headlines = soup.find_all(headline_tag, class_=headline_class)
        else:
            headlines = soup.find_all(headline_tag)

        print("Top News Headlines:")
        for i, headline in enumerate(headlines[:10], start=1):
            print(f"{i}. {headline.get_text(strip=True)}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    except Exception as e:
        print(f"Error parsing data: {e}")

if __name__ == "__main__":
    news_url = "https://indianexpress.com/"
    headline_tag = "h2"
    headline_class = None

    fetch_headlines(news_url, headline_tag, headline_class)
