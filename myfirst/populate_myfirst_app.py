import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myfirst.settings')
import django
django.setup()

import random
from myfirst_app.models import AccessRecord,Webpage,Topic
from faker import Faker

fakegen = Faker()
topics = ['Search','Social','Marketplace','News','Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        top = add_topic()
        fakeurl = fakegen.url()
        fakedate = fakegen.date()
        fakename = fakegen.company()

        webpg = Webpage.objects.get_or_create(topic=top,url=fakeurl,name=fakename)[0]

        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fakedate)[0]


if __name__ == '__main__':
    print("Populating Script!")
    populate(20)
    print('Populating Complete!')

