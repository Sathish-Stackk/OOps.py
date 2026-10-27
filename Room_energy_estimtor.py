fans = int(input("Number of fans: "))
lights = int(input("Number of lights: "))
hours = float(input("Usage hours: "))

fan_units = fans * 0.075 * hours
light_units = lights * 0.01 * hours
total = fan_units + light_units

print("Fan usage:", round(fan_units, 2), "units")
print("Light usage:", round(light_units, 2), "units")
print("Estimated usage:", round(total, 2), "units")
