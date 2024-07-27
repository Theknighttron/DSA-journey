def UniqueEmailAddress(emails):
    Unique = set()

    for email in emails:
        local, domain = email.split("@")
        local = local.split("+")[0]
        local = local.replace(".", "")
        Unique.add((local, domain))
    return len(Unique)
