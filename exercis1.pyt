def main():
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    
    rainfall = []

    for month in months:
        amount = float(input(f"Enter the rainfall for {month}: "))
        rainfall.append(amount)

    total_rainfall = sum(rainfall)
    average_rainfall = total_rainfall / 12
    max_rainfall = max(rainfall)
    min_rainfall = min(rainfall)
    max_month = months[rainfall.index(max_rainfall)]
    min_month = months[rainfall.index(min_rainfall)]

    print("\n--- Rainfall Statistics ---")
    print(f"Total rainfall: {total_rainfall:.2f}")
    print(f"Average monthly rainfall: {average_rainfall:.2f}")
    print(f"Highest rainfall: {max_rainfall:.2f} in {max_month}")
    print(f"Lowest rainfall: {min_rainfall:.2f} in {min_month}")

main()
