from faker import Faker
import json
import random
from datetime import datetime

fake = Faker()

payment_event = {
    "transaction_id": f"TXN{random.randint(100000,999999)}",
    "event_timestamp": datetime.utcnow().isoformat(),
    "sender_account": f"ACC{random.randint(10000,99999)}",
    "receiver_account": f"ACC{random.randint(10000,99999)}",
    "amount": round(random.uniform(100, 10000), 2),
    "currency": "INR",
    "merchant_id": f"MERCHANT{random.randint(100,999)}",
    "payment_method": random.choice(["UPI", "CARD", "NETBANKING"]),
    "transaction_status": random.choice(["SUCCESS", "FAILED"]),
    "location": fake.city(),
    "event_type": "PAYMENT"
}

print(json.dumps(payment_event, indent=2))