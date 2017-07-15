def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

#1a. we can give the numbers directly
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# we can also ask for an input
print("We can just give the function numbers directly:")
cheese_and_crackers(int(input("Please enter number of cheeses you have")), 30)
