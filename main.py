import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def get_html(url):
    r = requests.get(url)
    if r.ok:  # 200  ## 403 404
        return r.text
    print(r.status_code)


def get_page_link(url, html):
    soup = BeautifulSoup(html, 'lxml')
    title = soup.find('div', {'class': 'article__title'}).text
    link_containers = soup.findAll('div', {'class': 'articles-list'})
    print(title)

    for link_container in link_containers:
        a_tag = link_container.find("a")

        if a_tag:
            link = a_tag.get("href")
            print(urljoin(url, link))
        else:
            pass


def main():
    url = 'https://korrespondent.net/tag/65757/'
    get_page_link(url, get_html(url))


if __name__ == '__main__':
    main()


