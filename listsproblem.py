#lists problem
list = []
n = int(input())
for i in range(n):
    command = input()

    sections = command.split()

    if sections[0] == "append":
        if len(sections) == 2:
            value = int(sections[1])
            list.append(value)

    elif sections[0] == "insert":
        if len(sections) == 3:
            index = int(sections[1])
            value = int(sections[2])
            list.insert(index, value)

    elif sections[0] == "remove":
        if len(sections) == 2:
            value = int(sections[1])
            list.remove(value)

    elif sections[0] == "sort":
        list.sort()

    elif sections[0] == "pop":
        list.pop()

    elif sections[0] == "reverse":
        list.reverse()

    elif sections[0] == "print":
        print(list)
