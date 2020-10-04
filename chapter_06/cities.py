cities = {
    'kyiv': {
        'country': 'ukraine',
        'population': 3_500_000,
        'fact': 'capital of Ukraine',
        },
    'paris': {
        'country': 'france',
        'population': 9_000_000,
        'fact': 'capital of France',
        },
    'london': {
        'country': 'great britain',
        'population': 12_000_000,
        'fact': 'capital of UK'
        },
    }

for city, city_info in cities.items():
    print(f"City: {city.title()}")
    country = city_info['country']
    population = city_info['population']
    fact = city_info['fact']
    print(f"\tCountry: {country.title()}")
    print(f"\tPopulation: {population}")
    print(f"\tFact: {fact}")