import requests
import csv
import json
from bs4 import BeautifulSoup


def get_html(url):
    headers = {"User-Agent":"Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "lxml")
    return soup


def write_to_json(data):
    with open("data_file.json", "w", encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)


def parse_page():
    url = "https://kaktus.media/?lable=8"
    site = get_html(url)
    all_urls = site.find_all("div", class_="t f_medium")

    urls = []
    for url1 in all_urls:
        x = url1.find("a").get("href")
        urls.append(x)

    titles = []
    photos = []
    descriptions = []
    all2_urls = []

    for url2 in urls[::-1]:
        obj = get_html(url2)
        iii = obj.find("div", itemprop="articleBody").find_all("p")
        for i in iii:
            ik = i.text
            if ik != '':
                descriptions.append(ik)
                break
            else:
                continue

        titles.append(obj.find("h1").find("span").text)
        photos.append(obj.find("div", class_="topic-content").find("a").get("href"))
        all2_urls.append(obj.find("link", rel="canonical").get("href"))

    data = [titles, all2_urls, descriptions, photos]
    write_to_json(data)
