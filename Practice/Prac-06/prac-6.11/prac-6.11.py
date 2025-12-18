# 练习 6.11：城市 
#   创建一个名为 cities 的字典，将三个城市名用作键。
#   对于每座城市，都创建一个字典，并在其中包含该城市所属的国家、
#   人口约数以及一个有关该城市的事实。表示每座城市的字典都应包含
#   country、population 和 fact 等键。将每座城市的名字以及相关信息都打印出来。

cities = {
    'Seattle': {
        'country': 'USA',
        'population': 700000,
        'fact': 'The city is on the Puget Sound.'
    },
    'London': {
        'country': 'UK',
        'population': 9000000,
        'fact': 'The city is the capital of the UK.'
    },
    'Tokyo': {
        'country': 'Japan',
        'population': 90000000,
        'fact': 'The city is the largest city in Japan.'
    },
}

for city, city_info in cities.items():
    print(f"\n{city}:")
    print(f"\tCountry: {city_info['country']}")
    print(f"\tPopulation: {city_info['population']}")
    print(f"\tFact: {city_info['fact']}")
print()