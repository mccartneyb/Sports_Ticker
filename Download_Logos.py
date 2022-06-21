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
MLB_AL_url = 'https://www.sportslogos.net/teams/list_by_league/53/American_League/AL/logos/'
MLB_NL_url = 'https://www.sportslogos.net/teams/list_by_league/54/National_League/NL/logos/'

Get_Logos(NFL_url, 'Football')
Get_Logos(MLB_NL_url, 'Baseball_NL')
Get_Logos(MLB_AL_url, 'Baseball_AL')
