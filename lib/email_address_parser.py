# your code goes here!
import re

class EmailAddressParser:
    def __init__(self, addresses):
        self.addresses = addresses

    def parse(self):
        # Split on commas or whitespace
        parts = re.split(r'[,\s]+', self.addresses.strip())

        # Regex pattern for emails (basic version)
        email_pattern = re.compile(r'^[^@\s]+@[^@\s]+\.[^@\s]+$')

        # Keep only valid emails, remove duplicates, sort
        emails = [p for p in parts if email_pattern.match(p)]
        unique_sorted = sorted(set(emails))

        return unique_sorted

