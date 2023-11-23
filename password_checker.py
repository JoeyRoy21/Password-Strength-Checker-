
import string

# Function to get the user's password

def get_user_password():
    password = input("Enter your password: ")
    return password

# Function to check if the password meets the minimum length criterion
def is_valid_length(password):
    return len(password) >= 8

# Function to check if the password has both uppercase and lowercase letters
def has_upper_and_lower(password):
    return any(char.isupper() for char in password) and any(char.islower() for char in password)

# Function to check if the password has at least one numerical digit
def has_digit(password):
    return any(char.isdigit() for char in password)

# Function to check if the password has at least one special character
def has_special_char(password):
    special_characters = set(string.punctuation)
    return any(char in special_characters for char in password)

# Main function that orchestrates the password strength checking
def main():
    password = get_user_password()

 # Check if the password meets all the specified criteria
    if is_valid_length(password) and has_upper_and_lower(password) and has_digit(password) and has_special_char(password):
        print("Password is strong! ✔")
    else:
        print("Password does not meet the criteria. Please ensure it has at least 8 characters, both uppercase and lowercase letters, a numerical digit, and a special character.")

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
