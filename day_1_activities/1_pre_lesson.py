# this is what we will use for the video intro to dictionaries
# dictiopnary = colletion og {key:value} ordered and changable w no duplicates
capitals = {'USA': 'Washington D.C.',
            'India': 'New Dheli',
            'china': 'Beijing',
            'Russia': 'Moscow'}

# print(capitals.get('india'))
# if capitals.get('Japan'):
#     print('the capital iexists')
# else:
#     print('the capital doesnt exist')

# capitals.update({'Germany': 'Berlin'})
# capitals.update({'USA': 'Detroit'})
# capitals.pop('china')
# capitals.popitem()
# capitals.clear()

# keys = capitals.keys()

# print(keys)

# for key in capitals.key():
#     print(key)

# values = capitals.value()
# for value in capitals.values():
#     print(value)

# items = capitals.items()
# print(items)
for key, value in capitals.items():
    print(f"{key}: {value}")

