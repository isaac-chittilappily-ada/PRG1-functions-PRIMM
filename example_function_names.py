"""
This file contains the Python functions that have been
given descriptive names based on their purpose from the in-class task.
"""


# Function 1
# This function adds two numbers together.
def add(a, b):
    return a + b


# Function 2
# This function returns a greeting for a given name.
def greet(name):
    return "Hello, " + name + "!"


# Function 3
# This function calculates the sum of all numbers in a list.
def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


# Function 4
# This function gets the length of a string.
def get_length(text):
    return len(text)


# Function 5
# This function checks if a number is even.
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


# Function 6
# This function finds the largest number in a list.
def find_largest(items):
    if len(items) == 0:
        return None
    biggest = items[0]
    for item in items:
        if item > biggest:
            biggest = item
    return biggest


# Function 7
# This function counts the number of words in a sentence.
def count_words(sentence):
    words = sentence.split()
    return len(words)


# Function 8
# This function counts the number of vowels in a string.
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for letter in text:
        if letter in vowels:
            count += 1
    return count


# Function 9
# This function returns a new list with each number squared.
def square_numbers(numbers):
    result = []
    for num in numbers:
        result.append(num * num)
    return result


# Function 10
# This function finds the smaller of two numbers.
def find_smaller(a, b):
    if a < b:
        return a
    else:
        return b


# Function 11
# This function checks if a password is at least 8 characters long.
def is_valid_password(password):
    if len(password) >= 8:
        return True
    else:
        return False


# Function 12
# This function counts the occurrences of a specific letter in a string.
def count_letter_occurrences(text, letter):
    count = 0
    for char in text:
        if char == letter:
            count += 1
    return count


# Function 13
# This function calculates the average of numbers in a list.
def calculate_average(numbers):
    total = 0
    count = 0
    for num in numbers:
        total += num
        count += 1
    # Handle the case of an empty list to avoid division by zero.
    if count == 0:
        return 0
    return total / count


# Function 14
# This function reverses a given word.
def reverse_word(word):
    reversed_word = ""
    for i in range(len(word) - 1, -1, -1):
        reversed_word += word[i]
    return reversed_word


# Function 15
# This function sorts a list of numbers using bubble sort.
def bubble_sort(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers) - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers
