list_of_names = ["დავითი", "სოფია", "დავითი", "ლუკა", "დავითი", "ანა"]
name_to_count = "დავითი"
count = list_of_names.count(name_to_count)
print(f"სახელი '{name_to_count}' სიაში გვხვდება {count}-ჯერ.")

numbers_list = [10, 20, 30, 40, 50]
numbers_list.reverse()
print("შებრუნებული სია:", numbers_list)

list_of_numbers = [1, 2, 3]
result = list_of_numbers * len(list_of_numbers)
print("გარდამეტებული სია:", result)

insert_arr = ["Python", "Java", "C++", "JavaScript"]
insert_arr.insert(2, "დავითი")
print("განახლებული პროგრამირების ენების სია:", insert_arr)

elements_list = [5, 10, 5, 20, 5, 30]
element_to_find = 5
element_count = elements_list.count(element_to_find)
elements_list.remove(element_to_find)
print(f"ელემენტი '{element_to_find}' გვხვდება {element_count}-ჯერ.")
print("განახლებული სია წაშლის შემდეგ:", elements_list)
