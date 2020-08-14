# if, elif, else Practice

a = "Life is too short, you need python"

if "wife" in a:     # False
    print("wife")
elif "python" in a and "you" not in a:  # True & False = False
    print("python")
elif "shirt" not in a:  # True
    print("shirt")
elif "need" in a:   # True, but ignored since 'elif'
    print("need")
else:               # False
    print("none")
