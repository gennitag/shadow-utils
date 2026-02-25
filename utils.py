"""
shadow-utils
Lightweight utility functions.
"""

import hashlib
import random
import string
from datetime import datetime


def generate_token(length=16):
    """Generate a random secure token."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


def hash_text(text):
    """Return SHA256 hash of a string."""
    return hashlib.sha256(text.encode()).hexdigest()


def timestamp():
    """Return current timestamp."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


if __name__ == "__main__":
    print("Generated Token:", generate_token())
    print("Hashed Example:", hash_text("shadow"))
    print("Timestamp:", timestamp())
