"""
Generate short codes for the URL shortener.
Using secrets.randbelow to generate a random short code.
"""
import secrets

ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def generate_short_code(length: int = 7) -> str:
    return ''.join(ALPHABET[secrets.randbelow(len(ALPHABET))] for _ in range(length))
