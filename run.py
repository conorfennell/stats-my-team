import json
import requests


response = requests.get('https://fantasy.premierleague.com/api/bootstrap-static/')

data_dict = json.loads(response.content)
teams = data_dict['teams']
players = data_dict['elements']


def first_choice_penalty_takers(players):
    return [player for player in players if player['penalties_order'] == 1]

def first_choice_free_kick_takers(players):
    return [player for player in players if player['direct_freekicks_order'] == 1]

def print_players_name(players):
    for player in players:
        first_name = player['first_name']
        second_name = player['second_name']
        news = player['news']
        print(f'{first_name} {second_name} {news}')



def get_penalty_takers(players, order=1):
    penalty_takers = []

    for player in players:
        if player['penalties_order'] == order:
            penalty_takers.append(player)
    
    return penalty_takers

def one_hundred_percent_chance_of_playing(players):
    playing_players = []

    for player in players:
        if player['chance_of_playing_this_round'] != 0:
            playing_players.append(player)
        else:
            print(player['news'])    
    
    return playing_players

penalty_takers = get_penalty_takers(players)




print_players_name(penalty_takers)
print(' ')

print_players_name(one_hundred_percent_chance_of_playing(penalty_takers))