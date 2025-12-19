import random
import string
chars= " "+string.ascii_letters + string.digits + string.punctuation
chars = list(chars)
key = chars.copy()
random.shuffle(key)   
print(f"chars:{chars}")
print(f"key:{key}")

def encrypt(message):
    original_message = input("Enter the message to encrypt: ")
    encrypted_message = ""
    for letter in original_message:
        index = chars.index(letter)
        encrypted_message += key[index]
    return encrypted_message
def decrypt(encrypted_message):
    decrypted_message = ""
    for letter in encrypted_message:
        index = key.index(letter)
        decrypted_message += chars[index]
    return decrypted_message
def main():
    while True:
        choice = input("Choose an option: (E)ncrypt, (D)ecrypt, (Q)uit: ").upper()
        if choice == 'E':
            message = input("Enter the message to encrypt: ")
            encrypted_message = encrypt(message)
            print(f"Encrypted message: {encrypted_message}")
        elif choice == 'D':
            encrypted_message = input("Enter the message to decrypt: ")
            decrypted_message = decrypt(encrypted_message)
            print(f"Decrypted message: {decrypted_message}")
        elif choice == 'Q':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()