def check_password_strength(password):
    score = 0
    feedback = []
    specials = '!@#$%^&*'
    
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

    if any(password in specials for char in password):
        score += 1
    else:
        feedback.append('Password should contain specials')

    if 0 <= score < 2:
        strength = 'Weak'
    
    if 2 <= score < 4:
        strength = 'Medium'
        
    if 4 <= score < 6:
        strength = 'Strong'

    return score, feedback, strength

# Test passwords
passwords = ["hello", "Hello123", "PASSWORD", "MyPass!123!"]
for pwd in passwords:
    score, issues, strength = check_password_strength(pwd)
    print(f"'{pwd}': Score {score}/5, strength = {strength}")
    for issue in issues:
        print(f"  - {issue}")
    print()
