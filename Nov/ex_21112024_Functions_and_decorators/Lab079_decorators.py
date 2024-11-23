
def extra_security(go):

    def wrapper():
        print("Ready to drive with licence, helmet, kneecap")
        go()
        print("Removed all the items")
    return wrapper()

@extra_security
def drive_scooty():
    print("Normal function, driving started")
    print("safe driving done")

print("________________________")

@extra_security
def drive_ola():
    print("driving ola")
