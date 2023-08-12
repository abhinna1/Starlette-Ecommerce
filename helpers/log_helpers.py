import csv
from datetime import datetime
from commons.log_descriptions import (
    get_register_success_log_description,
    get_register_failed_log_description,
)
import time

from models.AuditLog import AuditLog

async def log_success_user_registration(email):
    log_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    description = get_register_success_log_description(email)
    log_data = [log_time, description]

    with open('audit_log.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(log_data)

async def log_failed_user_registration(email, message):
    log_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    description = get_register_failed_log_description(email)
    log_data = [log_time, description, message]

    with open('audit_log.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(log_data)
        
        
async def log_add_to_cart(email, product, message=None):
    if message:
        log_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        description = f"User {email} failed to add {product} to cart."
        log_data = [log_time, description, message]
        with open('audit_log.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(log_data)
        return
    log_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    description = f"User {email} successfully added {product} to cart."
    log_data = [log_time, description]

    with open('audit_log.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(log_data)
    
async def create_audit_log(message, email=None):
    log_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    description = message
    log_data = [log_time, description]

    with open('audit_log.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(log_data)

# def create_audit_log(db, message: str, created_by: str = None):
#     if len(message) < 1:
#         raise Exception('Message cannot be empty')

#     if created_by is not None and len(created_by) < 1:
#         raise Exception('Created by cannot be empty')
#     import pdb; pdb.set_trace()

#     new_log = AuditLog(message=message, created_by=created_by)
#     db.add(new_log)
#     db.commit()
#     db.refresh(new_log)
#     return new_log

        
# def create_audit_log(request, message, created_by):
#     log_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     method = request.method
#     path = request.url.path
#     status_code = response.status_code
#     log_data = [log_time, method, path, status_code]

    # with open('audit_log.csv', mode='a', newline='') as file:
    #     writer = csv.writer(file)
    #     writer.writerow(log_data)