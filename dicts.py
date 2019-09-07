cities = {'city':'Moscow', 'temperature':'20'}
print(cities['city'])
cities['temperature'] = str(int(cities['temperature']) - 5)
print(cities)

print(cities['country'])   
print(cities.get('country', 'Russia'))
cities['country'] = 'Russia'
cities['date'] = '07.09.2019'
print(cities)
print(len(cities))