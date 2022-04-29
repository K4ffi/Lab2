def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")
def get_user_input():
    userInput = input()
    splitInput = userInput.split(",")
    floatList = float(splitInput)
    return floatList

def calc_average(tempList):
    for number in tempList:
        i = i + 1
        total = total + number
        average = total/i
        return average

def find_min_max(tempList):
    minMax = [int(min(tempList)), int(max(tempList))]
    return minMax

def sort_temperature():
    print("sort_temperature")
def calc_median_temperature():
    print("calc_median_temperature")
