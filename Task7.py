import requests


url = "https://jsonplaceholder.typicode.com/posts"

def fetch_data(api_url):
    try:
        
        response = requests.get(api_url)
        response.raise_for_status() 
        return response.json() 
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None


if __name__ == "__main__":
    print("Fetching data from API...")
    data = fetch_data(url)

    if data:
        print("\nRaw JSON Response:")
        print(data) 
    else:
        print("No data to display.")
