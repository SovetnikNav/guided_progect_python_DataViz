import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]


# plt.scatter(x_values, y_values, c='red', edgecolor='none', s=40)
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)
plt.axis([0, 1100, 0, 1100000])


while True:
    answer = input("Save (y/n): ")
    if answer == "n":
        plt.show()
        break
    elif answer == "y":
        plt.savefig('squares_plot.png', bbox_inches='tight')
        break
    if answer != "y" or "n":
        print(answer)
        continue


