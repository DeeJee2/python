import numpy as np

def generate_magic_square(n):
    magic_square = np.zeros((n, n), dtype=int)

    i, j = 0, n // 2

    for num in range(1, n**2 + 1):
        magic_square[i, j] = num
        i, j = (i - 1) % n, (j + 1) % n

        if magic_square[i, j] != 0:
            i = (i + 2) % n
            j = (j - 1) % n

    return magic_square

def encrypt_with_magic_square(message, magic_square):
    n = len(magic_square)
    encrypted_message = ""

    for char in message:
        if char.isalpha():
            char = char.upper()
            indices = np.where(magic_square == ord(char) - ord('A') + 1)
            if indices[0].size > 0 and indices[1].size > 0:
                encrypted_message += f"{indices[0][0] + 1}{indices[1][0] + 1} "
        elif char.isspace():
            encrypted_message += ' '
        else:
            encrypted_message += char

    return encrypted_message.strip()

def decrypt_with_magic_square(encrypted_message, magic_square):
    n = len(magic_square)
    decrypted_message = ""

    for coords in encrypted_message.split():
        row, col = map(int, coords)
        decrypted_message += chr(magic_square[row - 1, col - 1] + ord('A') - 1)

    return decrypted_message

# Введення повідомлення користувачем
message = input("Введіть повідомлення для шифрування: ")
magic_square_size = 5

magic_square = generate_magic_square(magic_square_size)
encrypted_message = encrypt_with_magic_square(message, magic_square)

print("Зашифроване повідомлення:", encrypted_message)

decrypted_message = decrypt_with_magic_square(encrypted_message, magic_square)
print("Дешифроване повідомлення:", decrypted_message)
