import csv

# ------------------------------------------------------------
# Hardcoded stock prices — a dictionary mapping each stock
# symbol to its price per share.
# ------------------------------------------------------------
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 175,
    "MSFT": 410,
}


def show_available_stocks():
    """Print every stock symbol and price the user can choose from."""
    print("Available stocks:")
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol}: ${price}")
    print()


def get_user_investments():
    """
    Repeatedly ask the user for a stock symbol and quantity,
    building up a list of purchases until they choose to stop.
    Returns a list of dictionaries like:
        {"symbol": "AAPL", "quantity": 10, "price": 180, "cost": 1800}
    """
    investments = []

    while True:
        symbol = input("Enter a stock symbol (or 'done' to finish): ").upper().strip()

        if symbol == "DONE":
            break

        if symbol not in STOCK_PRICES:
            print(f"'{symbol}' isn't in our price list. Please choose from the list above.\n")
            continue

        quantity_input = input(f"How many shares of {symbol}? ").strip()

        if not quantity_input.isdigit():
            print("Please enter a whole number for quantity.\n")
            continue

        quantity = int(quantity_input)
        if quantity <= 0:
            print("Quantity must be greater than zero.\n")
            continue

        price = STOCK_PRICES[symbol]
        cost = price * quantity

        investments.append({
            "symbol": symbol,
            "quantity": quantity,
            "price": price,
            "cost": cost,
        })

        print(f"Added: {quantity} shares of {symbol} @ ${price} = ${cost}\n")

    return investments


def display_summary(investments, total):
    """Print a clean summary of every investment and the grand total."""
    print("\n--- Investment Summary ---")
    if not investments:
        print("No investments were entered.")
        return

    for item in investments:
        print(f"{item['symbol']}: {item['quantity']} shares x ${item['price']} = ${item['cost']}")

    print(f"\nTotal Investment Value: ${total}")


def save_to_txt(investments, total, filename="investment_summary.txt"):
    with open(filename, "w") as f:
        f.write("Investment Summary\n")
        f.write("------------------\n")
        for item in investments:
            f.write(f"{item['symbol']}: {item['quantity']} shares x ${item['price']} = ${item['cost']}\n")
        f.write(f"\nTotal Investment Value: ${total}\n")
    print(f"Saved to {filename}")


def save_to_csv(investments, total, filename="investment_summary.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Symbol", "Quantity", "Price", "Cost"])
        for item in investments:
            writer.writerow([item["symbol"], item["quantity"], item["price"], item["cost"]])
        writer.writerow([])
        writer.writerow(["Total Investment Value", "", "", total])
    print(f"Saved to {filename}")


def main():
    print("Welcome to the Stock Tracker!\n")
    show_available_stocks()

    investments = get_user_investments()
    total = sum(item["cost"] for item in investments)

    display_summary(investments, total)

    if investments:
        choice = input(
            "\nSave this summary to a file? (txt / csv / no): "
        ).lower().strip()

        if choice == "txt":
            save_to_txt(investments, total)
        elif choice == "csv":
            save_to_csv(investments, total)
        else:
            print("Summary not saved.")

    print("\nThanks for using the Stock Tracker!")


if __name__ == "__main__":
    main()