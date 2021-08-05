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


    def check_balance_old(self):
        square_open = re.findall('\[', self.string)
        square_close = re.findall('\]', self.string)
        figure_open = re.findall('\{', self.string)
        figure_close = re.findall('\}', self.string)
        circle_open = re.findall('\(', self.string)
        circle_close = re.findall('\)', self.string)

        if len(square_open) != len(square_close):
            print('Несбалансированно')

        elif len(figure_open) != len(figure_close):
            print('Несбалансированно')

        elif len(circle_open) != len(circle_close):
            print('Несбалансированно')

        else:
            print('Сбалансированно')



if __name__ == '__main__':
    skobki = input('Введите последовательность скобок: ')
    balance = IsBalanced(skobki)
    balance.check_balance()



