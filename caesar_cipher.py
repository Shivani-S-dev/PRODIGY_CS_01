"""
Author: [Your Name]
Task: Prodigy Infotech Cybersecurity Internship – Task 1
Description: This program encrypts and decrypts messages using the Caesar Cipher algorithm.
"""

def encrypt(message, shift):
    """
    Encrypts the input message by shifting each character by 'shift' positions.
    """
    encrypted_message = ""
    for char in message:
        if char.isupper():
            # Shift uppercase characters
            new_char = chr((ord(char) - 65 + shift) % 26 + 65)
            encrypted_message += new_char
        elif char.islower():
            # Shift lowercase characters
            new_char = chr((ord(char) - 97 + shift) % 26 + 97)
            encrypted_message += new_char
        else:
            # Non-alphabet characters remain the same
            encrypted_message += char
    return encrypted_message


def decrypt(message, shift):
    """
    Decrypts the input message by shifting each character backwards by 'shift' positions.
    """
    return encrypt(message, -shift)


def main():
    """
    Main function to handle user input and perform encryption or decryption.
    """
    print("🔐 Welcome to the Caesar Cipher Tool 🔐")
    print("---------------------------------------")
    
    message = input("Enter your message: ")
    
    while True:
        try:
            shift = int(input("Enter shift value (integer): "))
            break
        except ValueError:
            print("Please enter a valid integer shift value.")
    
    print("\nWhat would you like to do?")
    print("1. Encrypt the message")
    print("2. Decrypt the message")
    
    choice = input("Enter your choice (1 or 2): ").strip()
    
    if choice == '1':
        encrypted_text = encrypt(message, shift)
        print("\n✅ Encrypted Message:", encrypted_text)
    elif choice == '2':
        decrypted_text = decrypt(message, shift)
        print("\n✅ Decrypted Message:", decrypted_text)
    else:
        print("\n❌ Invalid choice. Please enter 1 or 2 only.")
    
    print("\nThank you for using the Caesar Cipher Tool!")

# Run the program
if __name__ == "__main__":
    main()
