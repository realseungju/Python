player = {
  'name':'seungju',
  'age': 21,
  'alive': True,
  'learned':["c","c++","java","python"],
  'friend': {
    'name':"seungju",
    'age':20,
    'fav_food': ["banana"]
  }
}

print(player.get('learned'))
player.pop('age')
print(player)
player['xp']=1000
print(player)
player['learned'].append("linux")
print(player)
print(player['friend']['name'])
player['friend']['fav_food'].append("apple")
print(player['friend']['fav_food'])