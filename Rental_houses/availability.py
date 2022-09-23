from Rental_houses.models import *


def house_availability(house):
    available_list = []
    houses = Houses.objects.filter(house_no=house)
    for house in houses:
        if house.occupancy == 'Vacant':
            available_list.append(True)
        else:
            available_list.append(False)

    return all(available_list)