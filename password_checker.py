import re

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters")

    if len(password) >= 12:
        score += 1
    else:
        feedback.append("12+ characters makes it much stronger")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one number")

    if re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]", password):
        score += 1
    else:
        feedback.append("Add at least one special character (!@#$ etc.)")

    common_passwords = ["password", "123456", "qwerty", "abc123", "password1"]
    if password.lower() in common_passwords:
        score = 0
        feedback = ["This is a very common password — change it immediately"]

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    print(f"\nPassword: {password}")
    print(f"Strength: {strength} ({score}/6)")

    if feedback:
        print("Suggestions:")
        for tip in feedback:
            print(f"  - {tip}")
    else:
        print("Great password! No suggestions.")

print("=== Password Strength Checker ===")
while True:
    pwd = input("\nEnter a password to check (or type 'quit' to exit): ")
    if pwd.lower() == "quit":
        print("Goodbye!")
        break
    check_password_strength(pwd)