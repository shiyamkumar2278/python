"""TASK 2 – Loops that Count Attempts
Problem Context: OTP Verification at a Bank Kiosk
"""

def verify_while():
    correct_otp = "123456"
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        otp = input("Enter OTP: ").strip()

        if otp == "":
            print("Blank input. Please enter OTP.")
            continue

        attempts += 1

        if otp == correct_otp:
            print("OTP verified successfully!")
            break
        else:
            print("Incorrect OTP.")
    else:
        print("Account locked for 30 minutes.")


def verify_for():
    correct_otp = "123456"

    for attempt in range(3):
        otp = input("Enter OTP: ").strip()

        if otp == "":
            print("Blank input. Attempt not counted.")
            continue

        if otp == correct_otp:
            print("OTP verified successfully!")
            break
        else:
            print("Incorrect OTP.")
    else:
        print("Account locked for 30 minutes.")


def verify_with_extra_attempts():
    correct_otp = "123456"
    security_answer = input(
        "Answer the security question correctly to get two extra attempts (yes/no): "
    ).strip().lower()

    if security_answer == "yes":
        max_attempts = 5
    else:
        max_attempts = 3

    attempts = 0

    while attempts < max_attempts:
        otp = input("Enter OTP: ").strip()

        if otp == "":
            print("Blank input. Attempt not counted.")
            continue

        attempts += 1

        if otp == correct_otp:
            print("OTP verified successfully!")
            break

        print("Incorrect OTP.")
    else:
        print("Account locked for 30 minutes.")


def verify_otp_recursive(correct_otp, remaining):
    if remaining == 0:
        print("Account locked for 30 minutes.")
        return

    otp = input("Enter OTP: ").strip()

    if otp == "":
        print("Blank input. Attempt not counted.")
        verify_otp_recursive(correct_otp, remaining)
        return

    if otp == correct_otp:
        print("OTP verified successfully!")
        return

    print("Incorrect OTP.")
    verify_otp_recursive(correct_otp, remaining - 1)


if __name__ == "__main__":
    print("OTP Verification")
    print("1. While loop")
    print("2. For loop")
    print("3. Two extra attempts after security answer")
    print("4. Recursion")
    choice = input("Choose an option: ").strip()

    if choice == "1":
        verify_while()
    elif choice == "2":
        verify_for()
    elif choice == "3":
        verify_with_extra_attempts()
    elif choice == "4":
        verify_otp_recursive("123456", 3)
    else:
        print("Invalid choice.")
