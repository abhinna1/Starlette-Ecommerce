import csv
from datetime import datetime
from commons.log_descriptions import (
    get_register_success_log_description,
    get_register_failed_log_description,
)
import time

async def log_success_user_registration(email):
    log_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    description = get_register_success_log_description(email)
    log_data = [log_time, description]

    with open('registration_log.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(log_data)

async def log_failed_user_registration(email, message):
    log_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    description = get_register_failed_log_description(email)
    log_data = [log_time, description, message]

    with open('registration_log.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(log_data)