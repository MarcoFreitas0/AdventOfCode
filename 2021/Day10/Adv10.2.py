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

def check_corruption(stk, lin, symb) :
    for char in lin :
        if char in symb.values() and symb[stk.peek()] != char :
            return True
        elif char in symb.values() :
            stk.pop()
        else :
            stk.push(char)
    return False

def fill_reward (incstk, rewlist, symb, rew) :
    while not incstk.isEmpty() :
        rewlist.append(symb[incstk.peek()])
        incstk.pop()
    line_reward = 0
    for symbol in rewlist :
        line_reward = line_reward * 5 + rew[symbol]
    return line_reward

ssymb = {'(' : ')','[' : ']','<' : '>','{' : '}'}
osymb = {')' : 1, ']' : 2, '>' : 4, '}' : 3}

scores = list()
for line in lines :
    stt = Stack()
    instt = list()
    if not check_corruption(stt, line, ssymb) :
        scores.append(fill_reward(stt, instt, ssymb, osymb))

scores.sort()
print(scores[int(len(scores)/2)])
