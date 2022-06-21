from sportsipy.nfl.schedule import Schedule
import datetime
from sportsipy.nfl.teams import Teams
from sportsipy.nfl.teams import Team

browns_schedule = Schedule('CLE', 2022)
for game in browns_schedule:
    if game.location == 'Home':
        print(f'{game.datetime.strftime("%m/%d")}  {game.opponent_abbr} vs CLE')
    else:
        print(f'{game.datetime.strftime("%m/%d")}  CLE @ {game.opponent_abbr}')