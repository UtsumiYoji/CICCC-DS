def main():
    weather = {
        "Monday": {"temperature": 20, "humidity": 60},
        "Tuesday": {"temperature": 22, "humidity": 55},
        "Wednesday": {"temperature": 19, "humidity": 65},
        "Thursday": {"temperature": 23, "humidity": 50},
        "Friday": {"temperature": 21, "humidity": 70}
    }

    # 1
    [print(v) for v in weather.values()]

    # 2
    max = 0
    for n, v in weather.items():
        if v["temperature"] > max:
            max = v["temperature"]
            day = n
    print('\nhighest temperature', day, max, '\n')

    # 3
    min = 100
    for n, v in weather.items():
        if v["humidity"] < min:
            min = v["humidity"]
            day = n
    print('lowest humidity', day, min, '\n')

    # 4
    weather["Wednesday"]['temperature'] = 25
    print(weather, '\n')

    # 5
    weather["Sunday"] = {"temperature": 24, "humidity": 60}
    print(weather)


if __name__ == '__main__':
    main()