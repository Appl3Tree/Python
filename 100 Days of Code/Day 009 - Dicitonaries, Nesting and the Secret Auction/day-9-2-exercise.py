#!/usr/bin/env python3

# Nesting  a list in a dictionary in a dictionary
travelLog = [
{
    'country': 'France',
    'visits': 12,
    'cities': ['Paris', 'Lille', 'Dijon']
},
{
    'country': 'Germany',
    'visits': 5,
    'cities': ['Berlin', 'Hamburg', 'Stuttgart']
},
]

def add_new_country(country, numVisits, city):
    new_country = {}
    new_country['country'] = country
    new_country['visits'] = numVisits
    new_country['cities'] = city
    travelLog.append(new_country)
    # My code to do the above 5 lines.
    #travelLog.append({'country': country, 'visits': numVisits, 'cities': city})

add_new_country('Russia', 2, ['Moscow', 'Saint Petersburg'])
print(travelLog)
