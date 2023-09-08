row1 = ["✉️", "✉️", "✉️"]
row2 = ["✉️", "✉️", "✉️"]
row3 = ["✉️", "✉️", "✉️"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure ?")
#in python whatever we input via input function it comes up as string so we need to convert it into int by typecasting
hor = int(position[0])
ver = int(position[1])

selected_row = map[ver]
selected_row[hor] = 'X'
print(f"{row1}\n{row2}\n{row3}")