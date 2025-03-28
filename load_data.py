import json

from models.nba.team import Team as NBATeam

def load_nba_teams(file_path):
    nba_teams = []
    with open(file_path) as fi:
        teams_json = json.load(fi)
        for team_json in teams_json:
            nba_team = NBATeam(**team_json)
            nba_teams.append(nba_team)
    return nba_teams

if __name__ == "__main__":
    load_nba_teams("data/nba/teams.json")