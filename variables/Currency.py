# Get amounts from user as floats to handle decimals
pesos = float(input('What do you have left in pesos? '))
soles = float(input('What do you have left in soles? '))
reais = float(input('What do you have left in reais? '))

# Conversion rates to USD
pesos_to_usd = 0.00025
soles_to_usd = 0.28
reais_to_usd = 0.21

# Calculate total in USD
total_usd = pesos * pesos_to_usd + soles * soles_to_usd + reais * reais_to_usd

# Print total with formatting
print(f"Total in USD: ${total_usd:.2f}")
