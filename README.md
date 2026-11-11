@@ -0,0 +1,8 @@
# Python Week 7 Assignment

- list_warmup.py: Demonstrates basic list operations including index retrieval, .append(), .remove(), and len().
- shopping_list.py: Implements an interactive shopping list manager with add, remove (with membership checks), show, and exit options.
- list_report.py: Processes a list to print numbered elements, counts items with names longer than 4 letters, and identifies the longest item name.
- README.md: Assignment documentation and reflections on list handling and safety checks.

It is safer to check using `in` before calling `.remove()` because attempting to remove an item that does not exist in the list will cause a ValueError and crash the program. Checking membership first ensures safe execution and allows you to handle missing items gracefully.
