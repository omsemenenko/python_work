rivers = {
    'dnipro': 'ukraine',
    'dunay': 'romania',
    'temse': 'united kingdom',
    }

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\nThe most biggest rivers in Europe are:")
for river in rivers.keys():
    print(river.title())

print("\nThe counties when rivers run are next:")
for country in rivers.values():
    print(country.title())