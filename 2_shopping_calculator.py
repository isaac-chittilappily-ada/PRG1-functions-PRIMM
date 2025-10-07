def calculate_total(price, tax_rate=0.20, discount=0, tip=0.12):
    subtotal = price - discount
    tax = subtotal * tax_rate
    total = subtotal + tax
    total += tip
    return total


def analyse_sales_data(sales: list):
    total = sum(sales)
    avg = total/len(sales)
    best_month = max(sales)
    worst_month = min(sales)

    return total, avg, best_month, worst_month

# Test cases
print(f"£{calculate_total(100):.2f}")
print(f"£{calculate_total(100, tax_rate=0.1):.2f}")
print(f"£{calculate_total(100, 0.08, 10):.2f}")