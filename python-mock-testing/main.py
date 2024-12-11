import requests


def add(a, b) -> int:
    return a + b


def get_joke() -> str:
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)
    joke = response.json()["value"] if response.status_code == 200 else "No jokes"
    return joke


def get_joke_advance() -> str:
    url = "https://api.chucknorris.io/jokes/random"
    try:
        response = requests.get(url, timeout=30)
        joke = response.json()["value"] if response.status_code == 200 else "No jokes"
        return joke
    except requests.exceptions.Timeout:
        return "Timeout exception"
    except requests.exceptions.ConnectionError:
        return "Connection error"


def len_joke() -> int:
    joke = get_joke()
    return len(joke)
