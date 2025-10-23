# Mini Project: Loan Calculation with Plot
import matplotlib.pyplot as plt

print("--- Loan Calculation ---")

while True:  # repeat for multiple scenarios
    capital = float(input("Initial capital (€): "))
    rate = float(input("Interest rate (%): ")) / 100
    years = int(input("Duration (years): "))
    limit = float(input("Safety limit (€): "))
    grace = int(input("Grace period (years): "))

    print("\n--- Capital evolution ---")
    
    capital_list = []  # store capital for plotting
    year_list = []

    current_capital = capital  # keep original capital
    for year in range(1, years + 1):    
        if year <= grace:
            print(f"Year {year}: (ignored – zero interest)")
        else:
            current_capital = current_capital * (1 + rate)
            print(f"Year {year}: {current_capital:.2f} €")

        capital_list.append(current_capital)
        year_list.append(year)

        if current_capital >= limit:
            print(">> Stop: safety limit exceeded!")
            break

    # Plot capital evolution
    plt.figure(figsize=(8,5))
    plt.plot(year_list, capital_list, marker='o', color='blue', linestyle='-')
    plt.xlabel("Year")
    plt.ylabel("Capital (€)")
    plt.title("Loan Capital Evolution Over Time")
    plt.grid(True)
    plt.show()

    print("\n--- End of scenario ---")

    again = input("Do you want to try another scenario? (y/n): ")
    if again.lower() != "y":
        break
