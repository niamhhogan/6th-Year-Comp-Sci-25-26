
# Enter name:

county = ["Dublin", "Laois", "Dublin", "Dublin", "Dublin", "Dublin", "Dublin", "Kildare", "Laois", "Kildare", "Dublin", "Laois", "Dublin"]

rent = [2500, 1200, 2000, 2100, 1900, 1999, 1790, 1500, 1000, 1390, 1980, 1105, 1999]

# Part i


# Part ii

print("-"*18)
print("{:<12}".format("County")+"{:<12}".format("Rent €"))
print("-"*18)
for index in range(len(county)):
    print("{:<12}".format(county[index])+"{:<12}".format(rent[index]))

# Part iii

# Part iv