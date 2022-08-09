import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','seventhprojectfaker.settings')

import django
django.setup()

from firstApp.models import *
from faker import Faker
from random import *
fake = Faker()
def phonenumber():
    first =str(randint(6,9))
    num = ""
    for i in range(0,9):
        num = str(randint(0,9))+num
    return str(first+num)
def fakedata(n):
    for i in range(n):
        fdate = fake.date()
        fcompany = fake.company()
        frole = fake.random_element(elements=('project manager','teamlead','software engineer','developer','tester','associate developer'))
        feligibility = fake.random_element(elements=('b.tech/fresher','b.tech/1 year exp','b.tech/2 year exp','b.tech/3 year exp','b.tech/4 year exp','m.tech/fresher','m.tech/1 year exp','m.tech/2 year exp','m.tech/3 year exp','m.tech/4 year exp','mca','phd'))
        faddress = fake.address()
        femail = fake.email()
        fphonnumber = phonenumber()
        if count == 0:
            che_record = chennai.objects.get_or_create(date = fdate, company= fcompany, role= frole, eligibility= feligibility, address= faddress, email=femail, phone=fphonnumber)
        if count == 1:
            hyd_record = hyderabad.objects.get_or_create(date = fdate, company= fcompany, role= frole, eligibility= feligibility, address= faddress, email=femail, phone=fphonnumber)
        if count == 2:
            del_record = delhi.objects.get_or_create(date = fdate, company= fcompany, role= frole, eligibility= feligibility, address= faddress, email=femail, phone=fphonnumber)
count = 0
while count<3:
    fakedata(10)
    count+=1
