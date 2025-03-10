import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoAdvanceModel2.settings')

import django
django.setup()

from testapp.models import Employees
import random
from faker import Faker

fk = Faker()

def populate(n):
    for i in range(n):
        fname = fk.name()
        fid = random.randint(0,9999)
        faddr = fk.city()
        Employees.objects.get_or_create(emp_id = fid, emp_name = fname, emp_addr = faddr)
n = int(input('n:'))
populate(n)
