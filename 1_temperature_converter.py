def celsius_to_fahrenheit(celsius: float) -> float:
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(farenheit: float) -> float:
    celsius = (farenheit - 32) / (9/5)
    return celsius


def km_to_miles(km: float) -> float:
    miles = km * 0.621371
    return round(miles, 2)

def miles_to_km(miles: float) -> float:
    km = miles / 0.621371
    return round(km, 2)

# Test the functions
print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(20))
print(celsius_to_fahrenheit(100))

print(fahrenheit_to_celsius(32))
print(fahrenheit_to_celsius(68))
print(fahrenheit_to_celsius(212))

print(km_to_miles(3))