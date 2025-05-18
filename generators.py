from faker import Faker


def fake_data():
    fake = Faker('ru_RU')
    email = fake.email()
    password = fake.password(length=10, special_chars=False)
    name = fake.first_name()
    return email, password, name
