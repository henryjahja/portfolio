import re

class Email:
    def __init__(self, email):
        self.original_email = email
        self.is_valid = self.valid(email)
        self.clean_email = self.clean(email)

    def valid(self, email):
        pattern = r'^[\w.%+-]+(\+[\w.%+-]+)?@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    def clean(self, email):
        cleaned = re.sub(r'\.', '', re.split(r'@|\+',email)[0]) + '@' + email.split('@')[1]
        return cleaned.lower()

emails = [
    'henry.jahjahmail.com@gg.com',
    'hen.ryjahja+7a.282@gmail.co',
    'hsjjj@g.co',
    'abc.abc@.abc',
    'some_email+some_thing@g.co.co.co'
]

for email in emails:
    x = Email(email)
    print(f'For email {email}:')
    print(f'\tOriginal Email: {x.original_email}')
    print(f'\tCleaned Email: {x.clean_email}')
    print(f'\t{"Email Valid" if x.is_valid else "Email Not Valid"}')
