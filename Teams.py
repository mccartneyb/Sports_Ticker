from sportsipy.nfl.teams import Teams
from sportsipy.nfl.teams import Team

teams = Teams()
for team in teams:
    t = Team(team.abbreviation)
    print(t.name, t.win_percentage)