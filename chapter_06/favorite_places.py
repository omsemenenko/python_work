favorite_places = {
    'kyiv': ['john', 'ivan', 'jim'],
    'london': ['sarah'],
    'paris': ['ken', 'edward'],
    }

for place, names in favorite_places.items():
    print(f"{place.title()} is a favorite place for:")
    for name in names:
        print(f"\t{name.title()}")