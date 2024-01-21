# your code goes here!

import re  # Import the regular expression module.

class EmailAddressParser:
    # Define a class-level regular expression for validating email addresses.
    email_regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    
    def __init__(self, emails):
        # Initialize the EmailAddressParser with a string of emails.
        self.emails = emails

    def parse(self):
        # Split the input string into a list of strings using commas or spaces as separators.
        strings = re.split(r',|\s', self.emails)
        
        parsed_emails = set()  # Create a set to store unique, valid email addresses.
        
        # Iterate over each string in the list.
        for string in strings:
            # Check if the string is a valid email address according to the email_regex.
            if self.email_regex.fullmatch(string):
                # If valid, add the email to the set of parsed emails.
                parsed_emails.add(string)

        # Convert the set of parsed emails to a sorted list and return it.
        return sorted(list(parsed_emails))

