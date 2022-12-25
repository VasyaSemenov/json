import json
from pprint import pprint
from random import randint as rd, choice as ch


def write(data, filename):
    data = json.dumps(data)
    data = json.loads(str(data))
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)


def read(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


class User:
    def __init__(self):
        self.name = ch(['Yan', 'Top', 'Alex', 'Jack', 'Cat'])
        self.age = rd(0, 80)
        self.id = rd(0, 1000000)


data = {
    'users': []
}


for i in range(100):
    data['users'].append(User().__dict__)

# write(data, 'data.json')


n_data = read('data.json')

print(n_data['users'][3])

g = User()
g.name = n_data['users'][0]['name']

print(g.name)
input()
