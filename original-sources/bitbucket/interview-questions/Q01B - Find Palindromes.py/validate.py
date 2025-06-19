from uuid import uuid4


if __name__ == "__main__": 
    import Palindrome
    import uuid
    import time
    words = [
    "Radar",
    "Refer",
    "Refere",
    "Racecar",
    "Racer",
    "Aibohphobia",
    "Noon",
    "Noun",
    "7abcdedcba",
    "a7bcdedcba",
    "ab7cdedcba",
    "abc7dedcba",
    "abcd7edcba",
    "abcde7dcba",
    "abcded7cba",
    "abcdedc7ba",
    "abcdedcb7a",
    "abcdedcba7"
    ]

    for word in words:
        if Palindrome.Palindrome.IsPalindrome(word):
            print("'{0:20}' is Palindrome".format(word))
        elif Palindrome.Palindrome.IsAlmostPalindrome(word):
            print("[v1]'{0:20}' is Almost palindrome".format(word))
            if Palindrome.Palindrome.IsAlmostPalindrome2(word):
                print("[v2]'{0:20}' is Almost palindrome".format(word))
            else:
                print("[v2]'{0:20}' ERROR in Almost palindrome".format(word))
        else:
            print("'{0:20}' is not a special word".format(word))



    print("="*36 + " Generating strings " + "="*36)
    print("*")
    print(time.strftime("%Y-%m-%d %H:%M:%S"))
    print("*")

    numbers = []
    for i in range(10000000, 100000000):
        numbers.append(f"{i:0>8d}")

    print("="*36 + "      Using v1      " + "="*36)
    print("*")
    print(time.strftime("%Y-%m-%d %H:%M:%S"))
    print("*")

    almost_palindrome1_count = 0
    start_1 = time.perf_counter_ns()
    for number in numbers:
        if Palindrome.Palindrome.IsAlmostPalindrome(number):
            almost_palindrome1_count +=1
    stop_1 = time.perf_counter_ns()

    print("="*36 + "      Using v2      " + "-"*36)
    print("*")
    print(time.strftime("%Y-%m-%d %H:%M:%S"))
    print("*")

    almost_palindrome2_count = 0
    start_2 = time.perf_counter_ns()
    for number in numbers:
        if Palindrome.Palindrome.IsAlmostPalindrome2(number):
            almost_palindrome2_count +=1
    stop_2 = time.perf_counter_ns()

    print("-"*36 + "      Complete      " + "-"*36)
    print("*")
    print(time.strftime("%Y-%m-%d %H:%M:%S"))
    print("*")
    print("-"*92)
    print("*")

    print(f"V1 elapsed time {((stop_1 - start_1)//1000000)/1000:7,.3f} seconds, and found {almost_palindrome1_count:,} almost palindrome numbers out of {len(numbers):,} numbers")
    print(f"V1 elapsed time {((stop_2 - start_2)//1000000)/1000:7,.3f} seconds, and found {almost_palindrome2_count:,} almost palindrome numbers out of {len(numbers):,} numbers")
    
