import json

players = [
    {
        'id' : 101,
        'name' : 'jiswal'
    },
    {
        'id' : 102,
        'name' : 'gill'
    }
]


player = {}
player['id'] = 103
player['name'] = "abhi"

players.append(player)
print(players)

for player in players:
    if player['id'] == 103:
        print(player)

player_dict = {101: players[0], 102: players[1], 103: players[2]}

print(player_dict[103])

