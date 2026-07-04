import csv

category_totals = {}

try:
    file = open("transactions.csv", "r")
    reader = csv.DictReader(file)

    for row in reader:
        try:
            category = row["category"]
            amount = float(row["amount"])

            if category in category_totals:
                category_totals[category] = category_totals[category] + amount
            else:
                category_totals[category] = amount

        except (ValueError, KeyError):
            print("Skipping invalid row:", row)

    file.close()   

    print("Total Amount Per Category")
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
