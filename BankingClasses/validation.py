""" This class validates the email addresses and password when logging on."""

class Validation:
    """ This class contains methods for validating email addresses and passwords."""
    @staticmethod
    def validate_email(email):
      if '@' in email:
        return True
      else:
        return False
    @staticmethod
    def validate_password(password):
      has_8 = len(password) >= 8
      has_upper = password.lower() != password
      has_lower = password.upper() != password
      has_special = False
      has_digit = False
      special_characters = "!@#$%^&*"
      for char in password:
        if char.isdigit():
          has_digit = True
          continue
        if char in special_characters:
          has_special = True
      """
      This method validates a password based on the following criteria:
      - The password must be at least 8 characters long.
      - The password must contain at least one uppercase letter,
        one lowercase letter, one digit, and one special character (!@#$%^&*).

      Args:
        password (str): The password to be validated.

      Returns:
        bool: True if the password is valid, False otherwise.
      """
      return has_8 and has_upper and has_lower and has_digit and has_special
