import sportsipy.mlb.schedule as mlb
import sportsipy.nfl.schedule as nfl
import sportsipy.ncaaf.schedule as ncaaf
from dateutil import parser
from sportsipy.ncaaf.teams import Teams

def get_browns_schedule(year):
    browns_schedule = nfl.Schedule('CLE', year)
    nfl_games = []
    for game in browns_schedule:
        #print(vars(game))
        nfl_games.append(game)
        if game.location == 'Home':
            print(f'{game.datetime.strftime("%m/%d")}  {game.opponent_abbr} vs CLE')
        else:
            print(f'{game.datetime.strftime("%m/%d")}  CLE @ {game.opponent_abbr}')
    return nfl_games

def get_indians_schedule(year):
    indians_schedule = mlb.Schedule('CLE', year)
    mlb_games = []
    for game in indians_schedule:
        if game.location == 'Home':
            print(f'{game.datetime.strftime("%m/%d")}  {game.opponent_abbr} vs CLE')
        else:
            print(f'{game.datetime.strftime("%m/%d")}  CLE @ {game.opponent_abbr}')

def get_buckeyes_schedule(year):
    teams = Teams()
    OSU = teams('OHIO-STATE')

    buckeyes_schedule = ncaaf.Schedule('OHIO-STATE', year)
    for game in buckeyes_schedule:
        game_time = parser.parse(game.date)
        if game.location == 'Home':
            print(f'{game_time.strftime("%m/%d")} {game.time} {game.opponent_name} vs {OSU.name}')
        else:
            print(f'{game_time.strftime("%m/%d")} {game.time} {OSU.name} @ {game.opponent_name}')