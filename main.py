import ciphers.caesar
import ciphers.playfair

def main():
    print("Welcome to the Cipher Tool!")

    while True:
        print("\nChoose an option:")
        print("1. Encryption")
        print("2. Decryption")
        print("3. Exit")

        option = input("Enter your choice: ")

        if option == "1":
            encryption_menu()
        elif option == "2":
            decryption_menu()
        elif option == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

def encryption_menu():
    while True:
        print("\nChoose a cipher algorithm for encryption:")
        print("1. Caesar Cipher")
        print("2. Playfair Cipher")
        print("3. Back to the main menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            text = input("Enter the text to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_text = ciphers.caesar.encrypt(text, shift)
            print("Encrypted text:", encrypted_text)

        elif choice == "2":
            text = input("Enter the text to encrypt: ")
            key = input("Enter the Playfair key: ")
            encrypted_text = ciphers.playfair.encrypt(text, key)
            print("Encrypted text:", encrypted_text)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please choose again.")

def decryption_menu():
    while True:
        print("\nChoose a cipher algorithm for decryption:")
        print("1. Caesar Cipher")
        print("2. Playfair Cipher")
        print("3. Back to the main menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            text = input("Enter the text to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted_text = ciphers.caesar.decrypt(text, shift)
            print("Decrypted text:", decrypted_text)
        elif choice == "2":
            text = input("Enter the text to decrypt: ")
            key = input("Enter the Playfair key: ")
            decrypted_text = ciphers.playfair.decrypt(text, key)
            print("Decrypted text:", decrypted_text)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please choose again.")


if __name__ == "__main__":
    main()
