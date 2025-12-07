import random
from faker import Faker
from django.core.management.base import BaseCommand
from api.models import Users, Phones, Cards, Friends, Workers

fake = Faker()

class Command(BaseCommand):
    help = 'Populate the database with random data'

    def handle(self, *args, **kwargs):
        # Create Users
        users = []
        for _ in range(100):
            user = Users(
                name=fake.first_name(),
                surname=fake.last_name(),
                username=fake.user_name(),
                birthday=fake.date_of_birth(minimum_age=18, maximum_age=80),
                passport_number=fake.bothify(text='??######'),
                id_number=fake.bothify(text='#########')
            )
            users.append(user)
        Users.objects.bulk_create(users)

        # Create Phones
        users = Users.objects.all()
        phones = []
        for user in users:
            for _ in range(random.randint(1, 3)):
                phone = Phones(
                    number=fake.phone_number(),
                    user=user
                )
                phones.append(phone)
        Phones.objects.bulk_create(phones)

        # Create Cards
        cards = []
        for user in users:
            for _ in range(random.randint(1, 2)):
                card = Cards(
                    bank=fake.company(),
                    number=fake.credit_card_number(),
                    expiry_date=fake.credit_card_expire(start='now', end='+5y', date_format='%Y-%m-%d'),
                    user=user
                )
                cards.append(card)
        Cards.objects.bulk_create(cards)

        # Create Friends
        friends = []
        for user in users:
            for _ in range(random.randint(1, 5)):
                friend = Friends(
                    fullname=fake.name(),
                    user=user
                )
                friends.append(friend)
        Friends.objects.bulk_create(friends)

        # Create Workers
        workers = []
        for _ in range(100):
            worker = Workers(
                username=fake.user_name(),
                is_admin=fake.boolean(chance_of_getting_true=25)
            )
            workers.append(worker)
        Workers.objects.bulk_create(workers)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with random data.'))