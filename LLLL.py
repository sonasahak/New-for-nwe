#city= [["Yerevan", "Abovyan"], ["Dilijan", "Armavir"], ["Talin", "Ijevan"]]
#for c in city:
 #   print(c)

cities= [["Yerevan", "Abovyan"], ["Dilijan", "Armavir"], ["Talin", "Ijevan"]]
#for country, city in cities:
  #  print("country is "+ country + " and city  is " +city )
my_dictionary= dict(cities)
print(my_dictionary)

for country, city in my_dictionary.items():
    print(country, city)
    for s in city:
        print(s)
        for country, city in my_dictionary.items():
            print(country, city)
            for s in city:
                print(s)

  for country, city in my_dictionary.items():
            print(country, city)
            for s in city:
                print(s)



  for country, city in my_dictionary.items():
            print(country, city)
            for s in city:
                print(s)