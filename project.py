import matplotlib.pyplot as plt
def add():
    subject = input("Enter subject: ")
    hours = float(input("Enter hours: "))

    f = open("study.txt", "a")
    f.write(subject + "," + str(hours) + "\n")
    f.close()

    print("Data added\n")

def view():
    try:
        f = open("study.txt", "r")
        data = f.readlines()
        f.close()

        total = 0

        for line in data:
            s, h = line.strip().split(",")
            print(s, "-", h)
            total = total + float(h)

        print("Total =", total, "hours\n")

    except:
        print("No data found\n")



def graph():
    try:
        f = open("study.txt", "r")
        data = f.readlines()
        f.close()

        subjects = []
        hours = []

        for line in data:
            s, h = line.strip().split(",")
            subjects.append(s)
            hours.append(float(h))

        plt.bar(subjects, hours)
        plt.show()

    except:
        print("No data for graph\n")


while True:
    print("1.Add")
    print("2.View")
    print("3.Graph")
    print("4.Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        add()

    elif ch == "2":
        view()

    elif ch == "3":
        graph()

    elif ch == "4":
        break

    else:
        print("Wrong choice\n")
