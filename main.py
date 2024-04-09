# Sum a List of Strings in Python

a_list = ['1', 'a', '2', 'c', '3', 4, 5]

total = 0

for item in a_list:
    if isinstance(item, int) or (
            hasattr(item, 'isdigit') and item.isdigit()
    ):
        total += int(item)

print(total) # 👉️ 15