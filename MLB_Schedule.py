from sportsipy.mlb.schedule import Schedule

indians_schedule = Schedule('CLE', 2022)
for game in indians_schedule:
    if game.location == 'Home':
        print(f'{game.datetime.strftime("%m/%d")}  {game.opponent_abbr} vs CLE')
    else:
        print(f'{game.datetime.strftime("%m/%d")}  CLE @ {game.opponent_abbr}')

