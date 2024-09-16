import re

# Function to check password strength
def check_password_strength(password):
    # Initialize variables for password strength criteria
    strength = 0
    feedback = []

    # Check length of the password
    if len(password) < 8:
        feedback.append("Password should be at least 8 characters long.")
    else:
        strength += 1

    # Check for lowercase letters
    if not re.search("[a-z]", password):
        feedback.append("Password should contain at least one lowercase letter.")
    else:
        strength += 1

    # Check for uppercase letters
    if not re.search("[A-Z]", password):
        feedback.append("Password should contain at least one uppercase letter.")
    else:
        strength += 1

    # Check for numbers
    if not re.search("[0-9]", password):
        feedback.append("Password should contain at least one number.")
    else:
        strength += 1

    # Check for special characters
    if not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        feedback.append("Password should contain at least one special character.")
    else:
        strength += 1

    # Evaluate overall strength and provide feedback
    if strength == 5:
        return "Password is strong!", feedback
    elif 3 <= strength < 5:
        return "Password is moderate. Consider improving based on the following:", feedback
    else:
        return "Password is weak. Improve based on the following:", feedback

# Main function to get user input and provide feedback
def password_assessment_tool():
    print("Password Strength Checker")
    password = input("Enter a password to check its strength: ")
    strength_message, suggestions = check_password_strength(password)

    # Print the password strength assessment and feedback
    print("\n" + strength_message)
    for suggestion in suggestions:
        print("- " + suggestion)

# Run the password assessment tool
if __name__ == "__main__":
    password_assessment_tool()
