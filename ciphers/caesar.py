# Define the alphabet
alphabet = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789ÁÉÍÓÚÑ-/\*+()$@#="?¿!%><_^:.,; '

# Define the key
# key = int(input("Enter the key length: "))


def encrypt(message, key):
    message = message.upper()
    ciphertext = ""
    for char in message:
        if char in alphabet:
            index = alphabet.index(char)
            new_index = (index + key) % len(alphabet)
            new_char = alphabet[new_index]
            ciphertext += new_char
        else:
            ciphertext += char
    return ciphertext


def decrypt(ciphertext, key):
    ciphertext = ciphertext.upper()
    plaintext = ""
    for char in ciphertext:
        if char in alphabet:
            index = alphabet.index(char)
            new_index = (index - key) % len(alphabet)
            new_char = alphabet[new_index]
            plaintext += new_char
        else:
            plaintext += char
    return plaintext


# message = input("Enter the message to encrypt: ")
# ciphertext = encrypt(message)
# print("The encrypted message is:", ciphertext)
# plaintext = decrypt(ciphertext)
# print("The decrypted message is:", plaintext)
