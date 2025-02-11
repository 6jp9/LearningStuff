import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'modelwithmysql.settings')
django.setup()

import faker
import random
from testapp.models import emp

fk = faker.Faker()

def dummy_data(n):
    for i in range(n):
        name = fk.name()
        id = fk.random_int(min=1,max=999)
        address = fk.address()
        contact = random.randint(6000000000,9999999999)
        emp.objects.get_or_create(empName=name,empID=id,empAddress=address,empContact=contact)

n = int(input('enter no of dummy data you want to enter:'))
dummy_data(n)



