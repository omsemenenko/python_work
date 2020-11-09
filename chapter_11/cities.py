from city_functions import get_formatted_city

print("Enter 'q' at any time to quit.")
while True:
    town = input("\nPlease a name of city: ")
    if town == 'q':
        break
    country = input("Please enter a name of country: ")
    if country == 'q':
        break

    formatted_city = get_formatted_city(town, country)
    print(f"\tNeatly formatted name: {formatted_city}.")
