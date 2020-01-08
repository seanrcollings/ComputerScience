message = "When you have a really giant line it can be" \
          "hard to read. So you can wrap a line with a slash"

print(message)

print("I can wrap an equation with the slash too")
answer = 123 + 892834 / 123 * 3213 / 31 ** 2 % 132 + \
    142 - 89432 * 382
print(answer)

print("I can wrap with ()")
answer = (123 + 892834 / 123 * 3213 / 31 ** 2 % 132 +
    142 - 89432 * 382)
print(answer)

print("{} works too")
answer = {123 + 892834 / 123 * 3213 / 31 ** 2 % 132 +
    142 - 89432 * 382}
print(answer)