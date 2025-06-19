import random

AnySizeInteger1111 = 2**96 + 2**64 + 2**32 + 1
AnySizeInteger9876543210 = 0
for i in range(10):
    AnySizeInteger9876543210 += i * (2 ** (32 * i))

print(f"AnySizeInteger1111       = {AnySizeInteger1111:,}")
print(f"AnySizeInteger9876543210 = {AnySizeInteger9876543210:,}")
