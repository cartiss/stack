from collections import deque

class Stack:

    def isEmpty(self, stack):
        if stack:
            return True
        else:
            return False

    def push(self, stack, new_el):
        stack = stack + list(new_el)

    def pop(self, stack):
        last_el = stack[-1]
        del stack[-1]
        return last_el

    def peek(self, stack):
        return stack[-1]

    def size(self, stack):
        return len(stack)

class IsBalanced(Stack):

    def __init__(self, skobki_list):
        self.skobki_list = skobki_list

    def isbalance(self):
        stack = deque()
        skobki_dict = {
            '{': 0,
            '}': 0,
            '[': 0,
            ']': 0,
            '(': 0,
            ')': 0,
        }

        for item in self.skobki_list:
            stack.append(item)

        while len(stack) != 0:
            last_el = stack.pop()

            skobki_dict[last_el] += 1

        if skobki_dict['['] != skobki_dict[']']:
            print('Несбалансировано')
        elif skobki_dict['{'] != skobki_dict['}']:
            print('Несбалансировано')
        elif skobki_dict['('] != skobki_dict[')']:
            print('Несбалансировано')
        else:
            print('Сбалансировано')



if __name__ == '__main__':
    skobki = '[][{}{]'
    balance = IsBalanced(skobki)
    balance.isbalance()



