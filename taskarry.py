from collections import Counter
numbers = [10, 45, 20, 70, 65]

largest = numbers[0]
second_largest = numbers[0]


# Find largest number
for num in numbers:
    if num > largest:
        largest = num

# Find second largest
for num in numbers:
    if num != largest:
        if second_largest == largest or num > second_largest:
            second_largest = num

print("Second Largest:", second_largest)


# Reverse a List (Without reverse() or Slicing)
numbers = [10, 20, 30, 40, 50]

left = 0
right = len(numbers) - 1

while left < right:

    temp = numbers[left]
    numbers[left] = numbers[right]
    numbers[right] = temp

    left += 1
    right -= 1

print(numbers)


# Remove Duplicates (Without set())
def remove_duplicates(lst):
    unique_items = []

    for item in lst:
        if item not in unique_items:
            unique_items.append(item)

    return unique_items

print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))



# Rotate List Left by k Positions
numbers = [10, 20, 30, 40, 50]
k = 2

n = len(numbers)

for i in range(k):

    first = numbers[0]

    for j in range(n - 1):
        numbers[j] = numbers[j + 1]

    numbers[n - 1] = first

print(numbers)



# Rotate List Right by k Positions
numbers = [10, 20, 30, 40, 50]
k = 2

n = len(numbers)

for i in range(k):

    last = numbers[n - 1]

    for j in range(n - 1, 0, -1):
        numbers[j] = numbers[j - 1]

    numbers[0] = last
print(numbers)


# Check if a Given String is a Palindrome
text = "madam"

reverse = ""

for ch in text:
    reverse = ch + reverse

if text == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")



# Count Vowels in a String
s = "Python is Fun!"
v = "aeiouAEIOU"
res = Counter([ch for ch in s if ch in v])
print(res)



# Check Palindrome. 
# same characters hote hain aur har character ki frequency bhi same hoti hai. Sirf unka order different ho sakta hai.
text1 = input("Enter first string: ")
text2 = input("Enter second string: ")

if sorted(text1) == sorted(text2):
    print("Anagram")
else:
    print("Not Anagram")




# Linear Search
numbers = [10, 20, 30, 40, 50]
target = 30

found = False

for i in range(len(numbers)):
    if numbers[i] == target:
        print("Element found at index:", i)
        found = True
        break

if not found:
    print("Element not found")



# Binary Search (Sorted List)
numbers = [10, 20, 30, 40, 50, 60, 70]
target = 50

low = 0
high = len(numbers) - 1

found = False

while low <= high:

    mid = (low + high) // 2

    if numbers[mid] == target:
        print("Element found at index:", mid)
        found = True
        break

    elif target < numbers[mid]:
        high = mid - 1

    else:
        low = mid + 1

if not found:
    print("Element not found")



    # Implement Bubble Sort

numbers = [50, 20, 40, 10, 30]

n = len(numbers)

for i in range(n - 1):

    for j in range(n - 1 - i):

        if numbers[j] > numbers[j + 1]:

            temp = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = temp

print("Sorted List:", numbers)



# Implement Selection Sort
numbers = [50, 20, 40, 10, 30]

n = len(numbers)

for i in range(n - 1):

    min_index = i

    for j in range(i + 1, n):

        if numbers[j] < numbers[min_index]:
            min_index = j

    temp = numbers[i]
    numbers[i] = numbers[min_index]
    numbers[min_index] = temp

print("Sorted List:", numbers)
