import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'DonaTracker_web.settings')
import django
django.setup()
from Main.models import Location, Donation
# from django.template.defaultfilters import slugify
import random
import csv

def populate():
    # First, we will create lists of dictionaries containing the pages
    # we want to add into each category.
    # Then we will create a dictionary of dictionaries for our categories.
    # This might seem a little bit confusing, but it allows us to iterate
    # through each data structure, and add the data to our models.
    
    # python_pages = [
    #     {"title": "Official Python Tutorial",
    #      "url":"http://docs.python.org/2/tutorial/"},
    #     {"title":"How to Think like a Computer Scientist",
    #      "url":"http://www.greenteapress.com/thinkpython/"},
    #     {"title":"Learn Python in 10 Minutes",
    #      "url":"http://www.korokithakis.net/tutorials/python/"} ]
    
    # django_pages = [
    #     {"title":"Official Django Tutorial",
    #      "url":"https://docs.djangoproject.com/en/1.9/intro/tutorial01/"},
    #     {"title":"Django Rocks",
    #      "url":"http://www.djangorocks.com/"},
    #     {"title":"How to Tango with Django",
    #      "url":"http://www.tangowithdjango.com/"} ]
    
    # other_pages = [
    #     {"title":"Bottle",
    #      "url":"http://bottlepy.org/docs/dev/"},
    #     {"title":"Flask",
    #      "url":"http://flask.pocoo.org"} ]
    
    # cats = {"Python": {"pages": python_pages},
    #         "Django": {"pages": django_pages},
    #         "Other Frameworks": {"pages": other_pages} }

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

    # for cat, cat_data in cats.items():
    #     c = add_cat(cat)
    #     for p in cat_data["pages"]:
    #         add_page(c, p["title"], p["url"])
    
    # # Print out the categories we have added.
    # for c in Category.objects.all():
    #     for p in Page.objects.filter(category=c):
    #         print("- {0} - {1}".format(str(c), str(p)))

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
    

# def add_page(cat, title, url):
#     p = Page.objects.get_or_create(category=cat, title=title)[0]
#     p.url=url
#     random.seed(str(url))
#     p.views = random.randint(0,150)
#     p.save()
#     return p

# def add_cat(name):
#     c = Category.objects.get_or_create(name=name)[0]
#     c.slug = slugify(name)
#     c.save()
#     return c

# Start execution here!
if __name__ == '__main__':
    print("Starting Main population script...")
    populate()