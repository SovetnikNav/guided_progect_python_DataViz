while True:
    answer = input("Save (y/n): ")
    if answer == "n":
        print("res n")
        break
    elif answer == "y":
        print("res y")
        break
    elif answer != "y" or "n":
        print(answer)
        continue