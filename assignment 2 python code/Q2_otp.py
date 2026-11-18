OTP = "246810"

def verify_while():
    attempts = 0
    while attempts < 3:
        value = input("Enter OTP: ").strip()
        if not value:
            print("Blank entry; not counted.")
            continue
        attempts += 1
        if value == OTP:
            print("Verified!")
            break
        print("Wrong OTP.")
    else:
        print("Account locked for 30 minutes.")

def verify_for():
    attempts = 0
    for _ in range(3):
        value = input("Enter OTP: ").strip()
        if not value:
            print("Blank entry; not counted.")
            # A for-loop consumes an iteration even on blank input.
            continue
        attempts += 1
        if value == OTP:
            print("Verified!")
            break
        print("Wrong OTP.")
    else:
        if attempts == 3:
            print("Account locked for 30 minutes.")
        else:
            print("Three nonblank attempts were not used; run again.")

def verify_security():
    allowed, used = 3, 0
    while used < allowed:
        value = input("Enter OTP: ").strip()
        if not value:
            print("Blank entry; not counted.")
            continue
        used += 1
        if value == OTP:
            print("Verified!")
            return
        print("Wrong OTP.")
        if used == 3:
            answer = input("Security question - registered city? ").strip().lower()
            if answer == "chennai":
                allowed += 2
                print("Two extra attempts granted.")
            else:
                break
    print("Account locked for 30 minutes.")

if __name__ == "__main__":
    print("1. while  2. for  3. security question")
    choice = input("Choose: ")
    if choice == "1": verify_while()
    elif choice == "2": verify_for()
    elif choice == "3": verify_security()
    else:
        pass
        print("Invalid choice.")
