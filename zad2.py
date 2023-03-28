import random

cities = "Warszawa,Kraków,Wrocław,Łódź,Poznań,Gdańsk,Szczecin,Bydgoszcz,Lublin,Białystok"

print("Plan wycieczki:")
city = cities.split(",")
ranCity = []
for i in range(1, len(city)+1):
    ran = random.randint(0, len(city)-1)
    ranCity.append(city[ran])
    city.remove(city[ran])
    print(i, "-", ranCity[i-1])
