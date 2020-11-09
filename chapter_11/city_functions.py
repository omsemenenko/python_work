def get_formatted_city(town, country, population=''):
    if population:
        full_name = f"{town}, {country} - population {population}"
    else:
        full_name = f"{town}, {country}"
    return full_name.title()