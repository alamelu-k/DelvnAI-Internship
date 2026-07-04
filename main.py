import csv

category_totals = {}

try:
    with open("transactions.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                category = row["category"].strip()
                amount = float(row["amount"])

                category_totals[category] = category_totals.get(category, 0) + amount

            except (ValueError, KeyError):
                print(f"Skipping invalid row: {row}")

    print("\nTotal Amount Per Category")
    print("-------------------------")

    sorted_totals = sorted(
        category_totals.items(),
        key=lambda item: item[1],
        reverse=True
    )

    for category, total in sorted_totals:
        print(f"{category}: {int(total)}")

except FileNotFoundError:
    print("Error: transactions.csv file not found.")
