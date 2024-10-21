import random

def generate_private_key(prime):
    return random.randint(2, prime - 2)

def generate_public_key(prime, base, private_key):
    return pow(base, private_key, prime)

def generate_shared_secret(prime, public_key, private_key):
    return pow(public_key, private_key, prime)

if __name__ == "__main__":
    prime = 23
    base = 5

    alice_private_key = generate_private_key(prime)
    alice_public_key = generate_public_key(prime, base, alice_private_key)

    bob_private_key = generate_private_key(prime)
    bob_public_key = generate_public_key(prime, base, bob_private_key)

    alice_shared_secret = generate_shared_secret(prime, bob_public_key, alice_private_key)
    bob_shared_secret = generate_shared_secret(prime, alice_public_key, bob_private_key)

    print(f"Alice's Private Key: {alice_private_key}")
    print(f"Alice's Public Key: {alice_public_key}")
    print(f"Bob's Private Key: {bob_private_key}")
    print(f"Bob's Public Key: {bob_public_key}")
    print(f"Alice's Shared Secret: {alice_shared_secret}")
    print(f"Bob's Shared Secret: {bob_shared_secret}")

    assert alice_shared_secret == bob_shared_secret, "Shared secrets do not match!"