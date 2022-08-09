import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','nineteenthORM.settings')

import django
django.setup()

from firstApp.models import *
from faker import Faker
from random import *
fake = Faker()
def fakedata(n):
    for i in range(n):
        fno = randint(1001,9999)
        fname = fake.name()
        fsal = randint(10000,20000)
        faddress = fake.address()
        emp_record = employee_model.objects.get_or_create(eno = fno, ename= fname, esal= fsal, eadd= faddress)
        fname=fname+'-Mngr'
        mng_record = manager_model.objects.get_or_create(eno = fno, ename= fname, esal= fsal, eadd= faddress)
fakedata(20)
