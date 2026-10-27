battery = int(input("Current battery (%): "))
hours = float(input("Hours used: "))

usage = (100 - battery) / hours if hours > 0 else 0
remaining = battery / usage if usage > 0 else 0

print("Average battery usage:", round(usage, 2), "%/hour")
print("Estimated remaining time:", round(remaining, 2), "hours")
