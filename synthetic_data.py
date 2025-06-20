from faker import Faker
fake = Faker()

def generate_user(user_id):
    return {
        "user_id": user_id,
        "name": fake.name(),
        "bank_account": fake.bban(),
        "income": round(fake.random_number(digits=5), 2),
        "transaction_history": [fake.sentence() for _ in range(3)],
        "pii": {"email": fake.email(), "phone": fake.phone_number()},
        "device_data": {"ip": fake.ipv4(), "device": fake.user_agent()}
    }
