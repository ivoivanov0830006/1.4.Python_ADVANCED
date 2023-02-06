from re import findall


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MoreThanOneAtSymbolError(Exception):
    pass


class InvalidNameError(Exception):
    pass


class InvalidDomainNameError(Exception):
    pass


pattern_name = r"[\w+\.]+"
pattern_domain_extension = r"\.[a-z]+"
pattern_domain_name = r"(?<=\@)\w{2,}"

valid_domains = [".com", ".bg", ".net", ".org"]

while True:
    email = input()
    if email == "End":
        break

    try:
        if email.count("@") > 1:
            raise MoreThanOneAtSymbolError("Email must contain only one @ symbol!")
        if len(email.split("@")[0]) <= 4:
            raise NameTooShortError("Name must be more than 4 characters!")
        if findall(pattern_name, email)[0] != email.split("@")[0]:
            raise InvalidNameError("Name must contain numbers, letter, underscores and dots!")
        if "@" not in email:
            raise MustContainAtSymbolError("Email must contain @!")
        if findall(pattern_domain_extension, email)[-1] not in valid_domains:
            raise InvalidDomainError(f"Domain must be one of the following: .com, .bg, .net, .org")
        if not findall(pattern_domain_name, email):
            raise InvalidDomainNameError("Domain name is not complete, must be at least 2 characters long!")

    except IndexError:
        print("Invalid email!")

    else:
        print("Email is valid")


"""
------------------------------------ Problem to resolve --------------------------------

You will be given some emails until you receive the command "End". Create the following custom 
exceptions to validate the emails:
NameTooShortError - raise it when the name in the email is less than or equal to 4 ("peter" will 
be the name in the email "peter@gmail.com")
MustContainAtSymbolError - raise it when there is no "@" in the email
InvalidDomainError - raise it when the domain of the email is invalid (valid domains are: .com, .bg, .net, .org)
When an error is encountered, raise it with an appropriate message:
NameTooShortError - "Name must be more than 4 characters"
MustContainAtSymbolError - "Email must contain @"
InvalidDomainError - "Domain must be one of the following: .com, .bg, .org, .net"
Hint: use the following syntax to add a message to the Exception: MyException("Exception Message")
If the current email is valid, print "Email is valid" and read the next one
-------------------------------------- Example inputs ----------------------------------
Input	
abc@abv.bg	
Output
Traceback (most recent call last):
  File ".\email_validator.py", line 20, in <module>
    raise NameTooShort("Name must be more than 4 characters")
__main__.NameTooShort: Name must be more than 4 characters
---------------------------------------------------------------
Input
peter@gmail.com
petergmail.com	
Output
Email is valid
Traceback (most recent call last):
  File ".\email_validator.py", line 18, in <module>
    raise MustContainAtSymbolError("Email must contain @")
__main__.MustContainAtSymbolError: Email must contain @
----------------------------------------------------------------
Input
peter@gmail.hotmail	
Output
Traceback (most recent call last):
  File ".\email_validator.py", line 22, in <module>
    raise InvalidDomainError("Domain must be one of the folowing: .com, .bg, .org, .net")
__main__.InvalidDomainError: Domain must be one of the folowing: .com, .bg, .org, .net

"""
