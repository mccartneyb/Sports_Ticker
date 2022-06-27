import os

from bs4 import BeautifulSoup
import requests
import urllib.request


def get_logos(url, sport):
    #create subdirectory
    if not os.path.exists(f'Logos/{sport}'):
        os.makedirs(f'Logos/{sport}')
    #get soup
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    #find section and get list items
    section = soup.find("div", id="team")
    list_items = section.findAll('li')

    #for each list item, get img src and title, save src image in sport directory as title
    for item in list_items:
        team = item.find('img')
        a = item.find('a')
        title = str(a["title"]).replace(' Logos','')
        urllib.request.urlretrieve(team['src'], f'Logos/{sport}/{title}.jpg')


NBA_url = 'https://www.sportslogos.net/teams/list_by_league/6/National_Basketball_Association/NBA/logos/'
NFL_url = 'https://www.sportslogos.net/teams/list_by_league/7/National_Football_League/NFL/logos/'
MLB_urls = ['https://www.sportslogos.net/teams/list_by_league/53/American_League/AL/logos/'
    , 'https://www.sportslogos.net/teams/list_by_league/54/National_League/NL/logos/']
CFB_urls = ['https://www.sportslogos.net/teams/list_by_league/30/NCAA_Division_I_a-c/NCAA_a-c/logos/'
    , 'https://www.sportslogos.net/teams/list_by_league/31/NCAA_Division_I_d-h/NCAA_d-h/logos/'
    , 'https://www.sportslogos.net/teams/list_by_league/32/NCAA_Division_I_i-m/NCAA_i-m/logos/'
    , 'https://www.sportslogos.net/teams/list_by_league/33/NCAA_Division_I_n-r/NCAA_n-r/logos/'
    , 'https://www.sportslogos.net/teams/list_by_league/34/NCAA_Division_I_s-t/NCAA_s-t/logos/'
    , 'https://www.sportslogos.net/teams/list_by_league/35/NCAA_Division_I_u-z/NCAA_u-z/logos/']

# Get Logos
get_logos(NFL_url, 'NFL')
get_logos(NBA_url, 'NBA')
for url in MLB_urls:
    get_logos(url, 'MLB')
for url in CFB_urls:
    get_logos(url, 'NCAAF')
