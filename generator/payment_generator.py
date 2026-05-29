from faker import Faker
import random
import json
import time
import os
from datetime import datetime
import signal
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from streaming.payment_producer import send_payment_event


fake = Faker()

BANKS = ["HDFC", "SBI", "KOTAK", "ICICI", "AXIS", "Saraswat"]


MERCHANT_CATEGORIES = [
    "Food",
    "Travel",
    "Shopping",
    "Bills",
    "Groceries",
    "Entertainment"
]

PAYMENT_METHODS = ["UPI", "CARD", "NETBANKING"]

TRANSACTION_STATUSES = [
    "SUCCESS",
    "FAILED",
    "REFUND",
    "REVERSAL"
]

OUTPUT_DIR = "data"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "raw_payments.ndjson")
os.makedirs(OUTPUT_DIR, exist_ok=True)


def generate_payment_event():
    event = {
        "transaction_id": f"TXN{random.randint(100000,999999)}",
        "event_timestamp": datetime.utcnow().isoformat(),
        "sender_account": f"ACC{random.randint(10000,99999)}",
        "receiver_account": f"ACC{random.randint(10000,99999)}",
        "amount": round(random.uniform(100, 10000), 2),
        "currency": "INR",
        "merchant_id": f"MERCHANT{random.randint(100,999)}",
        "payment_method": random.choice(PAYMENT_METHODS),
        "transaction_status": random.choice(TRANSACTION_STATUSES),
        "location": fake.city(),
        "device_id": f"DEV{random.randint(1000,9999)}",
        "event_type": "PAYMENT",
        "bank_name": random.choice(BANKS),
        "merchant_category": random.choice(MERCHANT_CATEGORIES),
        "processing_time_ms": random.randint(50, 500)
    }
    return event


def save_event_to_file(event):
    with open(OUTPUT_FILE, "a", encoding="utf-8") as file:
        file.write(json.dumps(event) + "\n")

def signal_handler(sig, frame):
    print("\nShutting down ...")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

if __name__ == "__main__":
    while True:
        payment_event = generate_payment_event()
        print(json.dumps(payment_event, indent=2))
        save_event_to_file(payment_event)
        send_payment_event(payment_event)
        time.sleep(1)








