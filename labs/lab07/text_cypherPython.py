import random

def generate_random_key(text):
    key = ''.join(random.choice(string.ascii_letters) for _ in range(len(text)))
    return key
def encrypt(text, key):
    encrypted_text = ''.join(chr(ord(text[i]) ^ ord(key[i])) for i in range(len(text)))
    return encrypted_text
def decrypt(encrypted_text, key):
    decrypted_text = ''.join(chr(ord(encrypted_text[i]) ^ ord(key[i])) for i in range(len(encrypted_text)))
    return decrypted_text

if __name__ == '__main__':
    import string
    text = input("Enter the text you want to encrypt: ")
    key = generate_random_key(text)
    encrypted_text = encrypt(text, key)
    
    print(f"Original Text: {text}")
    print(f"Encrypted Text: {encrypted_text}")
    print(f"Key: {key}")
    decrypted_text = decrypt(encrypted_text, key)
    print(f"Decrypted Text: {decrypted_text}")