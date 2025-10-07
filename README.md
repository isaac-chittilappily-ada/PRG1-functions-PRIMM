# PRIMM Activities for Python Functions

The PRIMM model (Predict, Run, Investigate, Modify, Make) is excellent for building programming understanding.

We have a mix of students with different abilities, and so therefore have provided a range of activities rising in difficulty. You are certainly **not** expected to complete all of these, depending on your experience, you might spend all of your class time looking at the first one or two. ***THAT IS FINE***.

## Activity 1: Temperature Converter 

### Code:
```python
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Test the function
print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(20))
print(celsius_to_fahrenheit(100))
```

### PRIMM Tasks:
**Predict:** What will each print statement output? Write down your predictions.

**Run:** Execute the code. Were your predictions correct?

**Investigate:** 
- What does the formula `(celsius * 9/5) + 32` do?
- What happens if you pass negative numbers?
- Try `celsius_to_fahrenheit(-40)`

**Modify:**
- Change the function to convert Fahrenheit to Celsius
- Add a second function that works the opposite way

**Make:**
- Create a function that converts kilometers to miles (multiply by 0.621371)

---

## Activity 2: Shopping Calculator 

### Code:
```python
def calculate_total(price, tax_rate=0.20, discount=0):
    subtotal = price - discount
    tax = subtotal * tax_rate
    total = subtotal + tax
    return total

# Test cases
print(f"£{calculate_total(100):.2f}")
print(f"£{calculate_total(100, 0.1):.2f}")
print(f"£{calculate_total(100, 0.08, 10):.2f}")
```

### PRIMM Tasks:
**Predict:** What will each print statement show? Pay attention to default parameters.

**Run:** Execute and check your predictions.

**Investigate:**
- What is `tax_rate=0.2` doing?
- What happens if you don't provide a discount?
- What does `:.2f` do in the print statements?

**Modify:**
- Add a tip parameter with a default of 12%

**Make:**
- Create a function that analyses sales data (total revenue, average sale, best/worst months)

---

## Activity 3: Password Validator 

### Code:
```python
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
```

### PRIMM Tasks:
**Predict:** For each test password, predict the score and what feedback will be given.

**Run:** Execute and compare with your predictions.

**Investigate:**
- What does `any()` do?
- How do `.isupper()`, `.islower()`, and `.isdigit()` work?
- Why does "PASSWORD" get a low score?

**Modify:**
- Add checking for special characters (!@#$%^&*)
- Return a strength rating ("Weak", "Medium", "Strong") based on score

**Make:**
- Create a function that generates a random secure password with specified requirements

---

## Activity 4: Data Analyser 

### Code:
```python
def analyse_scores(scores):
    if not scores:
        return {"error": "No scores provided"}
    
    total = sum(scores)
    average = total / len(scores)
    highest = max(scores)
    lowest = min(scores)
    
    # Count grades
    grade_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for score in scores:
        if score >= 90:
            grade_counts["A"] += 1
        elif score >= 80:
            grade_counts["B"] += 1
        elif score >= 70:
            grade_counts["C"] += 1
        elif score >= 60:
            grade_counts["D"] += 1
        else:
            grade_counts["F"] += 1
    
    return {
        "average": round(average, 2),
        "highest": highest,
        "lowest": lowest,
        "total_students": len(scores),
        "grade_distribution": grade_counts
    }

# Test data
test_scores = [85, 92, 78, 90, 87, 95, 82, 88, 91, 79]
empty_list = []

print("Test Results:")
print(analyse_scores(test_scores))
print("\nEmpty List Test:")
print(analyse_scores(empty_list))
```

### PRIMM Tasks:
**Predict:** What statistics will be calculated for the test_scores? What happens with empty_list?

**Run:** Execute and verify your predictions.

**Investigate:**
- How does the grade counting logic work?
- Why check `if not scores:` at the beginning?
- What does `round(average, 2)` do?

**Modify:**
- Add median calculation
- Include percentage for each grade in the distribution
- Add a "passing_rate" (scores >= 60)

**Make:**
- Create a function that calculates the final grade with weighted assignments (homework 30%, tests 70%)

---

## Activity 5: Text Processor 

### Code:
```python
def text_statistics(text):
    # Clean and prepare text
    words = text.lower().replace(',', '').replace('.', '').replace('!', '').replace('?', '').split()
    
    # Basic stats
    char_count = len(text)
    word_count = len(words)
    sentence_count = text.count('.') + text.count('!') + text.count('?')
    
    # Word frequency
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    
    # Find most common word
    most_common = max(word_freq.items(), key=lambda x: x[1]) if word_freq else ("", 0)
    
    # Average word length
    avg_word_length = sum(len(word) for word in words) / len(words) if words else 0
    
    return {
        "characters": char_count,
        "words": word_count,
        "sentences": sentence_count,
        "avg_word_length": round(avg_word_length, 2),
        "most_common_word": most_common[0],
        "most_common_count": most_common[1],
        "word_frequencies": word_freq
    }

# Test text
sample_text = "Hello world! This is a test. Hello again, world. This test is working!"
print(text_statistics(sample_text))
```

### PRIMM Tasks:
**Predict:** What statistics will be calculated? Which word will be most common?

**Run:** Execute and check your predictions.

**Investigate:**
- How does `.get(word, 0)` work for counting?
- What does `lambda x: x[1]` do in the `max()` function?
- Why use `if words else 0` for average calculation?

**Modify:**
- Add reading level calculation (average words per sentence)
- Find the longest and shortest words
- Calculate percentage of unique words

**Make:**
- Create a function that analyzes a CSV file of student data and returns insights

---

## Activity 6: Game Score Manager 

### Code:
```python
class ScoreManager:
    def __init__(self):
        self.players = {}
    
    def add_player(self, name):
        if name not in self.players:
            self.players[name] = []
            return f"Added player: {name}"
        return f"Player {name} already exists"
    
    def add_score(self, name, score):
        if name in self.players:
            self.players[name].append(score)
            return f"Score {score} added for {name}"
        return f"Player {name} not found"
    
    def get_player_stats(self, name):
        if name not in self.players or not self.players[name]:
            return f"No data for {name}"
        
        scores = self.players[name]
        return {
            "total_games": len(scores),
            "average_score": round(sum(scores) / len(scores), 2),
            "best_score": max(scores),
            "worst_score": min(scores),
            "improvement": scores[-1] - scores[0] if len(scores) > 1 else 0
        }
    
    def get_leaderboard(self):
        leaderboard = []
        for name, scores in self.players.items():
            if scores:
                avg_score = sum(scores) / len(scores)
                leaderboard.append((name, round(avg_score, 2)))
        
        return sorted(leaderboard, key=lambda x: x[1], reverse=True)

# Test the system
game = ScoreManager()
print(game.add_player("Alice"))
print(game.add_player("Bob"))
print(game.add_score("Alice", 85))
print(game.add_score("Alice", 92))
print(game.add_score("Bob", 78))
print(game.add_score("Bob", 88))

print("\nPlayer Stats:")
print("Alice:", game.get_player_stats("Alice"))
print("Bob:", game.get_player_stats("Bob"))

print("\nLeaderboard:")
for rank, (name, avg) in enumerate(game.get_leaderboard(), 1):
    print(f"{rank}. {name}: {avg}")
```

### PRIMM Tasks:
**Predict:** What will happen when you run this code? Who will be on top of the leaderboard?

**Run:** Execute and verify your predictions.

**Investigate:**
- How does the `__init__` method work?
- What's the difference between this and regular functions?
- How does `sorted(..., reverse=True)` work?

**Modify:**
- Add a method to remove players
- Add tracking for games won/lost instead of just scores
- Add date tracking for when scores were added

**Make:**
- Create a library management system that tracks books, borrowers, and due dates

---

