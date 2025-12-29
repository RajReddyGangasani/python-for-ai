class email_validator:
    def __init__(self):
        self.errors= []

    def validate_email(self, email):
        self.email = email
        if not "@" in email:
            self.errors.append("Fraud Email: {email}")
            return False
        return True
    
    def validate_age(self, age):
        self.age= age
        if age > 150: 
            self.errors.append(f"invalidage: {age}")
            return False
        return True
    
    def get_errors(self):
        return self.errors

validator = email_validator()

validator. validate_email(email= "bad-email")
validator. validate_age(age= 200)

print(validator.get_errors())