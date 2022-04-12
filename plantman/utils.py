import random
import string

def generate_uid(len: int = 12) -> str:
    return "".join(random.choices(string.ascii_uppercase, k=len))