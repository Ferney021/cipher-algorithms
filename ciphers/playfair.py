M_SIZE = 5
def create_playfair_matrix(key):
    # Remove duplicate letters from the key
    key = "".join(dict.fromkeys(key))

    # Create the initial matrix with the unique key letters
    matrix = list(key)

    # Fill in the remaining letters of the alphabet (omit 'J')
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for letter in alphabet:
        if letter not in matrix:
            matrix.append(letter)

    # Create a 5x5 matrix
    playfair_matrix = [matrix[i:i+5] for i in range(0, M_SIZE * M_SIZE, M_SIZE)]
    print(playfair_matrix)
    return playfair_matrix

def find_positions(matrix, letter):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == letter:
                return i, j

def playfair_encrypt(plain_text, key):
    matrix = create_playfair_matrix(key)
    cipher_text = []
    plain_text = plain_text.replace("J", "I")  # Replace 'J' with 'I' for consistency

    # Break the plain text into digraphs
    digraphs = []
    i = 0
    while i < len(plain_text):
        if i == len(plain_text) - 1 or plain_text[i] == plain_text[i + 1]:
            digraphs.append(plain_text[i] + "X")
            i += 1
        else:
            digraphs.append(plain_text[i] + plain_text[i + 1])
            i += 2

    # Encrypt each digraph
    for digraph in digraphs:
        a, b = digraph[0], digraph[1]
        row_a, col_a = find_positions(matrix, a)
        row_b, col_b = find_positions(matrix, b)

        if row_a == row_b:
            # Same row, shift right
            cipher_text.append(matrix[row_a][(col_a + 1) % M_SIZE] + matrix[row_b][(col_b + 1) % M_SIZE])
        elif col_a == col_b:
            # Same column, shift down
            cipher_text.append(matrix[(row_a + 1) % M_SIZE][col_a] + matrix[(row_b + 1) % M_SIZE][col_b])
        else:
            # Forming a rectangle, swap columns
            cipher_text.append(matrix[row_a][col_b] + matrix[row_b][col_a])

    return "".join(cipher_text)

def playfair_decrypt(cipher_text, key):
    matrix = create_playfair_matrix(key)
    plain_text = []
    to_iterate = [cipher_text[i:i+2] for i in range(0, len(cipher_text), 2)]
    # Decrypt each digraph
    for digraph in to_iterate:
        a, b = digraph[0], digraph[1]
        row_a, col_a = find_positions(matrix, a)
        row_b, col_b = find_positions(matrix, b)
        

        if row_a == row_b:
            # Same row, shift left
            plain_text.append(matrix[row_a][(col_a - 1) % M_SIZE] + matrix[row_b][(col_b - 1) % M_SIZE])
        elif col_a == col_b:
            # Same column, shift up
            plain_text.append(matrix[(row_a - 1) % M_SIZE][col_a] + matrix[(row_b - 1) % M_SIZE][col_b])
        else:
            # Forming a rectangle, swap columns
            plain_text.append(matrix[row_a][col_b] + matrix[row_b][col_a])
        
        # to_iterate.pop(0)
        # to_iterate.pop(1)

    return "".join(plain_text)

# Example usage:
key = "CRYPTOGRAPHY"
plaintext = "LAURA ES MONITORA BRILLANTE"
plaintext = plaintext.replace(' ', '')
encrypted_text = playfair_encrypt(plaintext, key)
decrypted_text = playfair_decrypt(encrypted_text, key)

print("Plaintext:", plaintext)
print("Encrypted:", encrypted_text)
print("Decrypted:", decrypted_text)
