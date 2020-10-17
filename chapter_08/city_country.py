def city_country(city, country):
    full_entries = f"{city.title()}, {country.title()}"
    return full_entries

country_city = city_country('santiago', 'chile')
print(country_city)

country_city = city_country('kyiv', 'ukraine')
print(country_city)

country_city = city_country('paris', 'france')
print(country_city)