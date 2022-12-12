
A = [11, 3, 4, 56+2j, "sunny", 4+2j]

# Print the index of all complex elements

# for i in A:
#     if type(i) == complex:
#         print(f"Element {i} Having Type {type(i)} At Index {A.index(i)}")

for i in A:
    if isinstance(i, (complex, int)):
        print(f"Element {i} Having Type {type(i)} At Index {A.index(i)}")