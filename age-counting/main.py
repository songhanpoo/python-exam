import requests

# Perform GET request
response = requests.get("https://coderbyte.com/api/challenges/json/age-counting")
data = response.json()
# Extract the data string
data_string = data["data"]

# Split the data string into individual items
items = data_string.split(", ")

# Count the items with age >= 50
count = 0
print(items)
for item in items:
    key, age = item.split("=")
    if key != "key":
      if int(age) >= 50:
          count += 1

# Print the final count
print("Number of items with age >= 50:", count)