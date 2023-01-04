import os
import requests
import argparse
from urllib.parse import urlparse
from dotenv import load_dotenv

load_dotenv()


def shorten_link(token, url):
    response = requests.post("https://api-ssl.bitly.com/v4/shorten",
                             headers={"Authorization": token},
                             json={"long_url": url})
    response.raise_for_status()
    return response.json()['link']


def count_clicks(token, url):
    parsed_url = urlparse(url)
    bitlink = '{}{}'.format(parsed_url.netloc, parsed_url.path)
    response = requests.get(f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary",
                            headers={"Authorization": token})
    response.raise_for_status()
    return response.json()['total_clicks']


def is_bitlink(token, url):
    parsed_url = urlparse(url)
    bitlink = '{}{}'.format(parsed_url.netloc, parsed_url.path)
    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}',
                            headers={"Authorization": token})
    return response.ok


if __name__ == '__main__':

    token = os.environ['BITLY_TOKEN']
    argstring_parsed = argparse.ArgumentParser()
    argstring_parsed.add_argument('name')
    url = argstring_parsed.parse_args().name
    if is_bitlink(token, url):
        print('Количество ссылок: ', count_clicks(token, url))
    else:
        print('Битлинк: ', shorten_link(token, url))