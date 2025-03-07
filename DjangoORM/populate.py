
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoORM.settings')

import django
django.setup()

from testapp.models import Employees
from faker import Faker
from random import *

fk = Faker()
def fakeinfo():
    fno = randint(101,999)
    fname = fk.name()
    fsal = randint(10,99)*1000
    fadder = fk.city()
    return Employees.objects.get_or_create(eno = fno, ename = fname, esal = fsal, eaddr = fadder)
n = int(input('n = '))
for i in range(n):
    fakeinfo()