fruits = ("apple", "banana", "fig", "cherry")
if "banana" in fruits:
    print("Yes, banana is in fruits!")
#part 3 of continues of tuple and tuples .py docs
fruits_l = list(fruits)
fruits_l[1] = "watermelon"
fruits = tuple(fruits_l)

print(fruits)
