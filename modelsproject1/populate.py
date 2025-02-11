import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'modelsproject1.settings')
import django
django.setup()
import faker
from testapp.models import Test_table_IT,Test_table_Gov
from random import *

fk = faker.Faker()
def dummy4IT():
    fname = fk.company()
    flocation = fk.city()
    fsalary = randint(10,100)*1000
    feligibility = fk.random_element(elements=('B-Tech','M-Tech','MCA','BSc'))
    flink = fk.url()
    Test_table_IT.objects.get_or_create(name = fname , location = flocation , salary = fsalary , eligibility = feligibility , link = flink)
def dummy4Gov():
    fname = fk.company()
    flocation = fk.city()
    feligibility = fk.random_element(elements=('B-Tech','M-Tech','MCA','BSc'))
    flink = fk.url()
    Test_table_Gov.objects.get_or_create(name = fname , location = flocation, eligibility = feligibility , link = flink)

n = int(input('enter a number of records:'))
for i in range(n):
    dummy4IT()
    dummy4Gov()