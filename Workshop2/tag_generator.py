tag = str(input("Enter an HTML tag: "))
value = str(input("Enter a value inside the HTML tag: "))

if tag:
    print(f"<{tag}>{value}</{tag}>")
