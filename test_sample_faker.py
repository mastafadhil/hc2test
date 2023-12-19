from seleniumbase import BaseCase
import sys
from faker import Faker
from pathlib import Path
from faker.providers import bank
from faker.providers import automotive
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

fake = Faker()
fake.add_provider(bank)
fake.add_provider(automotive)

"""print(fake.aba())
print(fake.first_name())
print(fake.email())
print(fake.address())
print(fake.url())"""
print(fake.first_name().upper()+fake.year())
print(fake.pystr_format(string_format=f"??###??#").upper())
print(fake.sentence())
print(fake.random_int(min=1, max=10))
