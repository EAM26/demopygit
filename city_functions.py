def show_location(city_name, country_name, population = ''):
    if population:
        return (f"{city_name.title()}, {country_name.title()}"
                f" - {population}")
    else:
        return (f"{city_name.title()}, {country_name.title()}")