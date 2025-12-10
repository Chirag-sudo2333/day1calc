fruits = {
    "Apple": {"Price": 20, "Qty": 12},
    "Banana": {"Price": 10, "Qty": 9},
    "Orange": {"Price": 15, "Qty": 20}
}
print("For Apple")
y = fruits["Apple"]["Price"]*fruits["Apple"]["Qty"]
print(y)
print("For Banana")
t = fruits["Banana"]["Price"]*fruits["Banana"]["Qty"]
print(t)
print("For Orange")
m = fruits["Orange"]["Price"]*fruits["Orange"]["Qty"]
print(m)
total_rev = y+t+m
print("Total revenue is", total_rev)
print(max(fruits, key=lambda x: fruits[x]["Qty"]*fruits[x]["Price"]))