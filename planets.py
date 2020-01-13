planet_list = ["Mercury", "Mars"]

planet_list.append("Jupiter")
planet_list.append("Saturn")

# print(planet_list)

planet_list.extend(["Uranus", "Neptune"])

# print(planet_list)

planet_list.insert(1,"Venus") 
planet_list.insert(2,"Earth") 

planet_list.append("Pluto")

rocky_planets = planet_list[0:4]

del planet_list[8]

