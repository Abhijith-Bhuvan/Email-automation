import requests
from bs4 import BeautifulSoup as bs


def get_stats_india():
    page = requests.get('https://www.worldometers.info/coronavirus/country/india/')

    soup = bs(page.text, 'html.parser')

    data = soup.findAll(class_='maincounter-number')
    numbers = {}

    numbers['Total'] = str(data[0].contents[1].text)
    numbers['Deaths'] = str(data[1].contents[1].text)
    numbers['Recovered'] = str(data[2].contents[1].text)

    for key in numbers:
        print(key, ' : ', numbers[key])
    # print(numbers)
    return numbers


if '__main__' == __name__:
    stats = get_stats_india()
