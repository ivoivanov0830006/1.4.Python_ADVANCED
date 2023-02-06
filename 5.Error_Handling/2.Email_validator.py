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
