text = input("Enter a string: ")

textContext = text.split()

for i in textContext:
    count = textContext.count(i)
    print(f"'{i}' appears {count} time(s)")