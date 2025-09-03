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

print(players)

with open('players.json', 'w') as file:
    json.dump(players, file)

with open('players.json', 'r') as reader:
    player_from_json = json.load(reader)
    print(player_from_json)
