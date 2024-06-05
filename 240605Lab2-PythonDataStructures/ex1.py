def main():
    students = {
        "Alice": [85, 78, 92],
        "Bob": [79, 74, 81],
        "Charlie": [91, 82, 85],
        "David": [76, 85, 83],
        "Eve": [88, 79, 92]
    }

    # 1
    averages = {k:sum(v)/len(v) for (k, v) in students.items()}
    print(averages, '\n')

    # 2
    max = 0
    for k, v in averages.items():
        if v > max:
            max = v
            student = k
    print('highest', student, max, '\n')

    # 3
    min = 100
    for k, v in averages.items():
        if v < min:
            min = v
            student = k
    print('lowest', student, min, '\n')

    # 4
    students['Frank'] = [80, 90, 85]
    print(students)


if __name__ == '__main__':
    main()