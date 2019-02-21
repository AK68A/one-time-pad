from numpy.random import randint

# This program demonstrates One-time Path encryption/decryption using string input
# I'm really proud of this program because it's actually my first program in Python
# This is also my first crypto program I've written ever, from scratch

# Global Variables
key = ''


# Convert plaintext message to a padded binary string
def plaintext_to_padded_binary(message):
    padded_binary_message_array = [bin(ord(ch))[2:].zfill(8) for ch in message]
    padded_binary_message_string = ''.join(padded_binary_message_array)
    return padded_binary_message_string


# Generate a random key of matching length to message
def generate_key(message):
    key_array_int = randint(0, 2, len(plaintext_to_padded_binary(message)))
    key_string = ''.join([str(numeric_string) for numeric_string in key_array_int])
    return key_string


# Encrypt message (create cipher)
def encrypt_message(padded_binary_string, key_string):
    i = 0
    cipher_string = ''
    while i < len(padded_binary_string):
        cipher_char = int(padded_binary_string[i]) ^ int(key_string[i])
        cipher_string += str(cipher_char)
        i += 1
    return cipher_string


# Decrypt message
def decrypt_message(encrypted_string, key_string):
    i = 0
    decrypted_binary_message_string = ''
    while i < len(encrypted_string):
        decrypted_char = int(encrypted_string[i]) ^ int(key_string[i])
        decrypted_binary_message_string += str(decrypted_char)
        i += 1
    return decrypted_binary_message_string


# Convert binary string to padded binary array
def create_array(decrypted_string):
    string = decrypted_string
    n = 8
    return [string[i:i + n] for i in range(0, len(string), n)]


# Convert padded binary array to non-padded binary array
def padded_binary_to_plaintext(decrypted_string_array):
    non_padded_binary_array = [padded_binary_string[:1] + "b" + padded_binary_string[1:]
                               for padded_binary_string in decrypted_string_array]
    unicode_array = binary_to_unicode(non_padded_binary_array)
    plaintext_message = unicode_to_plaintext(unicode_array)
    return plaintext_message


# Convert non-padded binary array indexes to unicode
def binary_to_unicode(non_padded_binary_array):
    unicode_array = [int(binary_string, 2) for binary_string in non_padded_binary_array]
    return unicode_array


# Convert unicode array to plaintext array
def unicode_to_plaintext(unicode_array):
    plaintext_array = [chr(ch) for ch in unicode_array]
    plaintext_message = ''.join(plaintext_array)
    return plaintext_message


# Encryption and decryption functions

def run_encryption(message):
    global key
    padded_binary_string = plaintext_to_padded_binary(message)
    key = generate_key(message)
    encrypted_string = encrypt_message(padded_binary_string, key)
    return encrypted_string


def run_decryption(encrypted_string, key_string):
    decrypted_string = decrypt_message(encrypted_string, key_string)
    decrypted_string_array = create_array(decrypted_string)
    message = padded_binary_to_plaintext(decrypted_string_array)
    return message


# Run the program


encrypted_message = run_encryption("Hello!")
decrypted_message = run_decryption(encrypted_message, key)

print(encrypted_message)
print(key)
print(decrypted_message)

