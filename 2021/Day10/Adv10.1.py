fhnd = open('input10.txt')

lines = [line.strip() for line in fhnd.readlines()]


class Stack :
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item) :
        self.items.append(item)

    def pop(self) :
        return self.items.pop()

    def peek(self) :
        return self.items[len(self.items) - 1]

def check_corruption(stk, lin, symb, rew) :
    for char in lin :
        if char in symb.values() and symb[stk.peek()] != char :
            return rew[char]
        elif char in symb.values() :
            stk.pop()
        else :
            stk.push(char)
    return 0

ssymb = {'(' : ')','[' : ']','<' : '>','{' : '}'}
osymb = {')' : 3, ']' : 57, '>' : 25137, '}' : 1197}

reward = 0
for line in lines :
    stt = Stack()
    reward += check_corruption(stt, line, ssymb, osymb)

print(reward)
