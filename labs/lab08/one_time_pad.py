import random

def generate_key(message_length):
    key = [random.randint(0, 255) for _ in range(message_length)]
    return bytes(key)

def one_time_pad_encrypt(message, key):
    encrypted_message = bytes(message[i] ^ key[i] for i in range(len(message)))
    return encrypted_message

def one_time_pad_decrypt(encrypted_message, key):
    decrypted_message = bytes(encrypted_message[i] ^ key[i] for i in range(len(encrypted_message)))
    return decrypted_message

# Example usage
message = b"This is a secret message"
key = generate_key(len(message))

encrypted_message = one_time_pad_encrypt(message, key)
decrypted_message = one_time_pad_decrypt(encrypted_message, key)

print("Original Message:", message)
print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message)