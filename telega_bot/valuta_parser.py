from bs4 import BeautifulSoup as bs
import requests
import json
import csv

main_url = 'https://valuta.kg/'


def get_html(url):
    respons = requests.get(url)
    return respons.text


def get_page_data(html):
    soup = bs(html, 'html.parser')
    get_kusre = soup.find('table', class_='vl-list').find('tbody').find_all('tr')
    list__ = []

    for kurs in get_kusre:
        try:
            find_all_kurse = kurs.find_all('td')
            bank = kurs.find('h4').find('a').text
            list_ = [bank]
        except AttributeError:
            continue
        for kurs in find_all_kurse:
            try:
                valutes = kurs.find('div', class_='td-rate__wrp').text
                for i in valutes.split():
                    if i.startswith(('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')):
                        list_.append(i)

            except AttributeError:
                continue

        with open('data.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow(list_)

        list__.append(list_)

    return list__


def main():
    with open ('data.csv', 'w') as file:
        pass
    data = get_page_data(get_html(main_url))
    return data


def get_buy_usd(data, b, a):

    usd_buy = []
    for i in data:
        ls = [i[b], float(i[a])]
        usd_buy.append(ls)

    best_buy = []
    for i in usd_buy:
        best_buy.append(i)

        if i[1] < best_buy[0][1]:
            best = i
    return best


def get_sell_usd(data, b, a):

    usd_sell = []
    for i in data:
        ls = [i[b], float(i[a])]
        usd_sell.append(ls)

    best_sell = []
    for i in usd_sell:
        best_sell.append(i)

        if i[1] > best_sell[0][1]:

            best = i

    return best


if __name__ == '__main__':
    # main()
    pass













