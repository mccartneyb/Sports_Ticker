from bs4 import BeautifulSoup
import requests
import urllib.request


def Get_Logos(url, sport):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    section = soup.find("div", id="team")
    teams = section.findAll('img')
    for i, team in enumerate(teams):
        print(sport, team['src'])
        urllib.request.urlretrieve(team['src'], f'Logos/{sport}_{i}.jpg')


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
Get_Logos(NFL_url, 'NFL')

for i, url in enumerate(MLB_urls):
    Get_Logos(url, f'MLB_{i}')

for i, url in enumerate(CFB_urls):
    Get_Logos(url, f'NCAAF_{i}')
