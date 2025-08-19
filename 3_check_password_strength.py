def check_password_strength(password):
    score = 0
    feedback = []
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters")
    
    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Password should contain uppercase letters")
    
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Password should contain lowercase letters")
    
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Password should contain numbers")
    
    return score, feedback

# Test passwords
passwords = ["hello", "Hello123", "PASSWORD", "MyPass123!"]
for pwd in passwords:
    score, issues = check_password_strength(pwd)
    print(f"'{pwd}': Score {score}/4")
    for issue in issues:
        print(f"  - {issue}")
    print()