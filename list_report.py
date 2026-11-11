@@ -0,0 +1,19 @@
items = ["bread", "avocado", "milk", "sweet potatoes", "tea"]

print("Numbered Items:")
for index, item in enumerate(items, start=1):
    print(f"{index}. {item}")

long_names_count = 0
for item in items:
    if len(item) > 4:
        long_names_count += 1

print(f"\nItems with more than 4 letters: {long_names_count}")

longest_item = items[0]
for item in items:
    if len(item) > len(longest_item):
        longest_item = item

print(f"The longest item name is: {longest_item}")
