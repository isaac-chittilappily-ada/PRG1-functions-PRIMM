from math import ceil

def analyse_scores(scores):
    if not scores:
        return {"error": "No scores provided"}
    
    count = len(scores)
    total = sum(scores)
    average = total / count
    highest = max(scores)
    lowest = min(scores)
    median = sorted(scores)[ceil(count / 2)]
    
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

    # Task 2
    # make a dictionary for percentage distribution of grades
    grade_dist = {key: round(value/count, 2) * 100 for key, value in grade_counts.items()}
    
    # Task 3
    # calculate pass rate
    passes = len([score for score in scores if score >= 60])
    passing_rate = round((passes/count) * 100, 2)

    return {
        "average": round(average, 2),
        "highest": highest,
        "lowest": lowest,
        "total_students": count,
        "grade_distribution": grade_counts,
        'grade_distribution': grade_dist,
        "median": median,
        'passing_rate': passing_rate
    }

# Test data
test_scores = [85, 92, 78, 90, 87, 95, 82, 59, 91, 79]
empty_list = []

print("Test Results:")
print(analyse_scores(test_scores))
print("\nEmpty List Test:")
print(analyse_scores(empty_list))
