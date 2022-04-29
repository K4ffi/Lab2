def main():
    display_main_menu()
    x = get_user_input()
    calc_average(x)
    find_min_max(x)

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    x = input()
    y = x.split(",")
    z = [float(i) for i in y]
    return z

def calc_average(tempList):
    for x in range (0, len(tempList)):
        total = total + tempList[x]
    average = total/len(tempList)
    return average

def find_min_max(tempList):
    minMax = [int(min(tempList)), int(max(tempList))]
    return minMax

def sort_temperature():
    print("sort_temperature")
def calc_median_temperature():
    print("calc_median_temperature")

if __name__ == "__main__":
    main()