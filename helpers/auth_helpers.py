import re
import bcrypt
import csv


def check_common_password(password):
    """
    Checks if the password exists in the common password CSV file, considering case changes
    and combinations of multiple common passwords.
    Returns True if the password is found, False otherwise.
    """
    with open('commons/common_passwords.csv', 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            common_password = row['password']
            # Check for exact match
            if common_password == password:
                return True
            # Check for case-insensitive match
            if common_password.lower() == password.lower():
                return True
    return False


def verify_password_strength(password):
    """
    Verifies that a password meets the complexity requirements and is not a common password.
    Returns True if the password is strong, False otherwise.
    """
    # Verify password length
    if not (8 <= len(password) <= 12):
        return False

    # Verify password complexity
    if not re.search(r'[A-Z]', password):  # Check for uppercase letters
        return False
    if not re.search(r'[a-z]', password):  # Check for lowercase letters
        return False
    if not re.search(r'\d', password):  # Check for numbers
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):  # Check for special characters
        return False

    return True


def hash_password(password:str) -> str:
    """
    Hashes a password using the SHA-256 algorithm.
    Returns the hashed password as a string.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode("utf-8")