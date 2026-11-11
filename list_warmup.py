@@ -0,0 +1,12 @@
fruits = ["apple", "banana", "mango", "orange"]

print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")

fruits.append("pineapple")
print("After append:", fruits)

fruits.remove("banana")
print("After remove:", fruits)

print(f"Total fruits remaining: {len(fruits)}")
