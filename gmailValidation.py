import re

class GmailValidator:
    @staticmethod
    def validate_email(email):
        # Regular expression for a basic email format
        email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@gmail\.com$')

        if email_pattern.match(email):
            print(f" '{email}' is a valid Gmail address.")
        else:
            print(f" '{email}' is not a valid Gmail address.")

# Example usage:
if __name__ == "__main__":
    user_input = input("Enter an email address: ")
    GmailValidator.validate_email(user_input)
