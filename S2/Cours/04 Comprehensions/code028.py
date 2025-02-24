parts = [
    "CPU",
    "GPU",
    "Motherboard",
    "RAM",
    "SSD",
    "Power Supply",
    "Case",
    "Cooling Fan",
]

stocks = [15, 8, 12, 30, 25, 10, 5, 20]

print({part: stock for part, stock in zip(parts, stocks)})
print({part: stock for part, stock in zip(parts, stocks) if part.lower().startswith("c") and stock > 10})

# ne fonctionne pas il parcourt tout le stcok pour chaque part
print({part: stock for part in parts for stock in stocks})
print({part: stock for part in parts if part.lower().startswith("c") for stock in stocks})

