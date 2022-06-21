from sportsipy.ncaaf.schedule import Schedule
from dateutil import parser
from sportsipy.ncaaf.teams import Teams
teams = Teams()
OSU = teams('OHIO-STATE')

buckeyes_schedule = Schedule('OHIO-STATE', 2021)
for game in buckeyes_schedule:
    game_time = parser.parse(game.date)
    if game.location == 'Home':
        print(f'{game_time.strftime("%m/%d")} {game.time} {game.opponent_name} vs {OSU.name}')
    else:
        print(f'{game_time.strftime("%m/%d")} {game.time} {OSU.name} @ {game.opponent_name}')
