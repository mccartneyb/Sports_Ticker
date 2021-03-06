import sportsipy.mlb.schedule as mlb
import sportsipy.nfl.schedule as nfl
import sportsipy.ncaaf.schedule as ncaaf
import sportsipy.nba.schedule as nba
from dateutil import parser
from sportsipy.ncaaf.teams import Teams
from pprint import pprint


def get_browns_schedule(year):
    browns_schedule = nfl.Schedule('CLE', year)
    nfl_games = []
    print(f'\nNFL\n')
    pprint(dir(browns_schedule._games[0]))
    for game in browns_schedule:
        # print(vars(game))
        this_game = {'date': game.date,
                     'opponent': game.opponent_name,
                     'location': game.location,
                     'result': game.result,
                     'points_for': game.points_scored,
                     'points_against': game.points_allowed}

        nfl_games.append(this_game)
        # if game.location == 'Home':
        #     print(f'{game.datetime.strftime("%m/%d")}  {game.opponent_abbr} vs CLE')
        # else:
        #     print(f'{game.datetime.strftime("%m/%d")}  CLE @ {game.opponent_abbr}')
    return nfl_games


def get_indians_schedule(year):
    indians_schedule = mlb.Schedule('CLE', year)
    mlb_games = []
    print(f'\nMLB\n')
    pprint(dir(indians_schedule._games[0]))
    for game in indians_schedule:
        this_game = {'date': game.date,
                     'opponent': game.opponent_abbr,
                     'location': game.location,
                     'result': game.result,
                     'points_for': game.runs_scored,
                     'points_against': game.runs_allowed
                     }
        mlb_games.append(this_game)
        # if game.location == 'Home':
        #     print(f'{game.datetime.strftime("%m/%d")}  {game.opponent_abbr} vs CLE')
        # else:
        #     print(f'{game.datetime.strftime("%m/%d")}  CLE @ {game.opponent_abbr}')
    return mlb_games


def get_buckeyes_schedule(year):
    buckeyes_schedule = ncaaf.Schedule('OHIO-STATE', year)
    ncaaf_games = []
    print(f'\nNCAAF\n')
    pprint(dir(buckeyes_schedule._games[0]))
    for game in buckeyes_schedule:
        this_game = {'date': game.date,
                     'opponent': game.opponent_name,
                     'location': game.location,
                     'result': game.result,
                     'points_for': game.points_for,
                     'points_against': game.points_against
                     }
        ncaaf_games.append(this_game)
        # game_time = parser.parse(game.date)
        # if game.location == 'Home':
        #     print(f'{game_time.strftime("%m/%d")} {game.time} {game.opponent_name} vs OSU')
        # else:
        #     print(f'{game_time.strftime("%m/%d")} {game.time} OSU @ {game.opponent_name}')
    return ncaaf_games

def get_cavs_schedule(year):
    cavs_schedule = nba.Schedule('CLE', year)
    nba_games = []
    print(f'\nNBA\n')
    pprint(dir(cavs_schedule._games[0]))
    for game in cavs_schedule:
        # print(vars(game))
        this_game = {'date': game.date,
                     'opponent': game.opponent_name,
                     'location': game.location,
                     'result': game.result,
                     'points_for': game.points_scored,
                     'points_against': game.points_allowed}

        nba_games.append(this_game)
        # if game.location == 'Home':
        #     print(f'{game.datetime.strftime("%m/%d")}  {game.opponent_abbr} vs CLE')
        # else:
        #     print(f'{game.datetime.strftime("%m/%d")}  CLE @ {game.opponent_abbr}')
    return nba_games

