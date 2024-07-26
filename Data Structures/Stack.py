class Stack:    
    def __init__(self, max=5) -> None:
        self.max = max
        self.__list = [None] * max
        self.__top = -1

    def push(self, data):
        if self.__top == self.max - 1:
            print("<stack overload>")
        else:
            self.__top += 1
            self.__list[self.__top] = data
            return data

    def pop(self):
        if self.__top == -1:
            print("<stack is empty>")
        else:
            self.__top -= 1

    def stack_list(self):
        return self.__list[:self.__top + 1]

    def display(self):
        if self.__top == -1:
            print("<stack is empty>")
        else:
            for i in range(self.__top, -1, -1):
                print(self.__list[i], end=' ')
            print()
