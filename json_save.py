import json

person = {
    'name': 'Max',
    'age': 10,
    'phones': ['7777', '112']
}

catalog = {
    'Milk': 150,
    'Water': 25,
    'Carrot': 40,
    'CocaCola': 90

}

result = json.dumps(person)

print(result)
print(type(result))

result_1 = json.dumps(catalog)
print(result_1)