
mixed_list = ['a', 'b', 3, 'e', 'i', 7, 'o', 'u', 9]
vowels = "aeiou"
vowel_count = sum(1 for item in mixed_list if isinstance(item, str) and item.lower() in vowels)
print(f"Number of vowels: {vowel_count}")


sequence_list = [1, 5, 3, 2, 5, 3, 8, 5, 3]
count_pairs = sum(1 for i in range(len(sequence_list) - 1) if sequence_list[i] == 5 and sequence_list[i + 1] == 3)
print(f"Count of 5 and 3 in a row: {count_pairs}")


mixed_elements = ['h', 3, 'e', 'l', 'l', 9, 'o']
joined_string = ''.join(str(item) for item in mixed_elements)
print(f"Single string representation: {joined_string}")


rows = 4
for _ in range(rows):
    print('*' * rows)


age = int(input("Enter your age: "))
if age > 12:
    print("You are not 12 years old")
else:
    print("You are 12 years old or younger")
