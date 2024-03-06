def create_geographic_dictionary(n, country_data):
    geo_dict = {}
    for i in range(n):
        country_info = country_data[i].split()
        country = country_info[0]
        cities = country_info[1].split(',')
        for city in cities:
            geo_dict[city]=country
    return geo_dict

def find_country_by_city(geo_dict, query):
    return geo_dict.get(query, "")

n=int(input("Введите количество стран: "))
country_data = []
for _ in range(n):
    country_data.append(input("Введите страну и список городов через пробел: "))

geo_dict = create_geographic_dictionary(n, country_data)

query_num = int(input("Введите количество запросов: "))
for _ in range(query_num):
    query = input("Введите название города: ")
    print(find_country_by_city(geo_dict, query))



