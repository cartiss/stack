import re

class Stack:

    def isEmpty(self, stack):
        if stack:
            return False
        else:
            return True

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

    def __init__(self, string):
        self.string = string
        self.square_skobki_open = []
        self.square_skobki_close = []
        self.figure_skobki_open = []
        self.figure_skobki_close = []
        self.circle_skobki_open = []
        self.circle_skobki_close = []

    def check_balance(self):
        if not self.isEmpty(self.string):
            for item in self.string:
                if item == '[':
                    self.square_skobki_open.append(item)

                elif item == ']':
                    self.square_skobki_close.append(item)

                elif item == '{':
                    self.figure_skobki_open.append(item)

                elif item == '}':
                    self.figure_skobki_close.append(item)

                elif item == '(':
                    self.circle_skobki_open.append(item)

                elif item == ')':
                    self.circle_skobki_close.append(item)


            if len(self.square_skobki_open) != len(self.square_skobki_close):
                print('Несбалансированно')

            elif len(self.figure_skobki_open) != len(self.figure_skobki_close):
                print('Несбалансированно')

            elif len(self.circle_skobki_open) != len(self.circle_skobki_close):
                print('Несбалансированно')

            else:
                print('Сбалансированно')


if __name__ == '__main__':
    skobki = '[][}{]'
    balance = IsBalanced(skobki)
    balance.check_balance()



