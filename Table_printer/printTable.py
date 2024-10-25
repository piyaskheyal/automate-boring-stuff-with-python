tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]


# Find the length of longest string
longest_string = 0
for i in tableData:
    for j in i:
        if(len(j)>longest_string):
            longest_string = len(j)

# Print the tabular data in right justified manner
for i in tableData:
    for j in i:
        print(j.rjust(longest_string), end=" ")
    print("\n")