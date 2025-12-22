# 练习 8.6：城市名 
#   编写一个名为 city_country() 的函数，它接受城市的名称及其所属的国家。
#   这个函数应返回一个格式类似于下面的字符串：
#       "Santiago, Chile"
#   至少使用三个城市至国家对调用这个函数，并打印它返回的值。

def city_country(city, country):
    print(f"{city.title()}, {country.title()}")

city_country('santiago', 'chile')
city_country('paris', 'france')
city_country('tokyo', 'japan')