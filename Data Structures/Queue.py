#BISMILLAH
class Queue:
    def __init__(self, max = 5) -> None:
        self.max = max
        self.__list = [None] * max
        self.__front = -1
        self.__rear = -1
        
    def insert(self, data):
        if self.__rear == self.max - 1:
            print("< queue is full > ")
        elif self.__front == -1 and self.__rear == -1:
            self.__front = 0
            self.__rear = 0
            self.__list[self.__rear] = data
        else:
            self.__rear += 1
            self.__list[self.__rear] = data

    def delete(self):
        if self.__front == -1 and self.__rear == -1:
            print("< queue is empty > ")
        else:
            print(self.__list[self.__front], "deleted")
            self.__front += 1
            if self.__rear < self.__front:
                self.__front = -1
                self.__rear = -1
                
    def peek(self):
        if self.__front == -1 and self.__rear == -1:
            print("< queue is empty > ")
        else:
            print(f"< {self.__list[self.__front]} is at the front >")
    
    def queue_list(self):
        return self.__list[self.__front:self.__rear + 1]
    
    def display(self):
        if self.__front == -1:
            print("< queue is empty > ")
        else:
            print("< Elements in the Queue are >")
            for i in range(self.__front, self.__rear + 1):
                print(self.__list[i])