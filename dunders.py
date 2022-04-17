# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(other.x + other.x, other.y + other.y)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    v1 = Vector(10, 20)
    v2 = Vector(20, 30)
    v3 = v1 + v2

    print(v3.x)
    print(v3.y)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
