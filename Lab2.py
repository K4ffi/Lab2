def main():
    display_main_menu()
    x = get_user_input()
    calc_average(x)
    find_min_max(x)
    y = sort_temperature(x)
    print(calc_median_temperature(y))


def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")


def get_user_input():
    x = input()
    y = x.split(",")
    z = [float(i) for i in y]
    return z


def calc_average(tempList):
    total = 0
    for x in range(0, len(tempList)):
        total += tempList[x]
    average = total/len(tempList)
    return average


def find_min_max(tempList):
    minMax = [int(min(tempList)), int(max(tempList))]
    return minMax


def sort_temperature(tempList):
    tempList.sort()
    return tempList


def calc_median_temperature(tempList):
    index = len(tempList) - 1
    if len(tempList) % 2 == 0:
        median = (tempList[int(len(tempList)/2)] + tempList[int(len(tempList)/2+1)]) / 2
    else:
        median = tempList[int(index/2)]
    return median


if __name__ == "__main__":
    main()