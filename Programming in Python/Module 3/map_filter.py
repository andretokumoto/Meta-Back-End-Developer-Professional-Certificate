list_country = ["Brasil","Uruguai","Japan","Egypt","Belgium","Butan"]

def find_country(country):
    if country[0] == 'B':
        return country

#Map
map_country = map(find_country,list_country)
print("Map")
print()

for country in map_country:
    print(country)
    
print()
print('Filter') 
print()
#Filter

filter_country = filter(find_country,list_country)

for country in filter_country:
    print(country)