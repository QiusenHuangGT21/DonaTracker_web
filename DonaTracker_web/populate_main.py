import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'DonaTracker_web.settings')
import django
django.setup()
from Main.models import Location, Donation
# from django.template.defaultfilters import slugify
import random
import csv

donation_names = ['donation1', 'donation2', 'donation3']

def populate():

    with open('location_data.csv') as file:
        data = []
        reader = csv.reader(file, delimiter=',')
        line_counter = 0
        for row in reader:
            if line_counter != 0:
                data.append(row)
            line_counter += 1
    
    for location in data:
        add_location(location)
        print("add " + location[1] + " to database")
    
    first_location = Location.objects.all()[0]

    for name in donation_names:
        add_donation(first_location, name)

def add_location(location_list):
    l = Location.objects.get_or_create(name = location_list[1])[0]
    l.key = int(location_list[0])
    # l.name = location_list[1]
    l.lat = float(location_list[2])
    l.lng = float(location_list[3])
    l.street_address = location_list[4]
    l.city = location_list[5]
    l.state = location_list[6]
    l.zip = int(location_list[7])
    l.type = location_list[8]
    l.phone = location_list[9]
    l.website = location_list[10]
    l.employees.add()
    l.save()
    return l

def add_donation(location_key, name):
    d = Donation.objects.get_or_create(short_description = name, location = location_key)[0]
    d.full_description = 'This is ' + name
    d.value = random.randint(10, 100) / 7.0
    d.save()
    return d


if __name__ == '__main__':
    print("Starting Main population script...")
    populate()