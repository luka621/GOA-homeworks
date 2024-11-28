age = 16
for i in range(1, age + 1):
    print(f"Year {i}")

temperature_celsius = 25.0
temperature_fahrenheit = (temperature_celsius * 9/5) + 32
print(f"Temperature in Fahrenheit: {temperature_fahrenheit}°F")

a, b, c = 5, 10, 15
print(f"{a} < {b}:", a < b)
print(f"{b} > {c}:", b > c)
print(f"{a} == {5}:", a == 5)

print(f"{a} < {b} and {b} < {c}:", a < b and b < c)
print(f"{a} > {b} or {b} < {c}:", a > b or b < c)
print(f"not {a} > {b}:", not (a > b))

n = 4
for i in range(1, n + 1):
    print("<3 " * i)

user_age = 20
is_twenty = user_age == 20
print(f"User is 20 years old: {is_twenty}")
