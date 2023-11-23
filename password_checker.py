
import string

def get_user_password():
    password = input("Enter your password: ")
    return password

def is_valid_length(password):
    return len(password) >= 8

def has_upper_and_lower(password):
    return any(char.isupper() for char in password) and any(char.islower() for char in password)

def has_digit(password):
    return any(char.isdigit() for char in password)

def has_special_char(password):
    special_characters = set(string.punctuation)
    return any(char in special_characters for char in password)

def main():
    password = get_user_password()

    if is_valid_length(password) and has_upper_and_lower(password) and has_digit(password) and has_special_char(password):
        print("Password is strong! ✔")
    else:
        print("Password does not meet the criteria. Please ensure it has at least 8 characters, both uppercase and lowercase letters, a numerical digit, and a special character.")

if __name__ == "__main__":
    main()
