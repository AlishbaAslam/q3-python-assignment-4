import random
import string

def generate_password(length=12, use_upper=True, use_digits=True, use_special=True):
    # Define the character pools
    lower_chars = string.ascii_lowercase
    upper_chars = string.ascii_uppercase if use_upper else ''
    digits = string.digits if use_digits else ''
    special_chars = string.punctuation if use_special else ''
    
    # Combine all allowed characters
    all_chars = lower_chars + upper_chars + digits + special_chars
    
    if not all_chars:
        raise ValueError("At least one character set must be selected.")
    
    # Generate a random password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    
    return password

def main():
    print("=== Password Generator ===")
    length = int(input("Enter password length (e.g., 12): "))
    
    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'
    
    password = generate_password(length, use_upper, use_digits, use_special)
    print("\nGenerated Password:", password)

if __name__ == "__main__":
    main()