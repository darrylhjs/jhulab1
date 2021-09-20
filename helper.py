class Empty(Exception):
    '''User-defined exception for "Empty" error when stack is empty'''
    pass

class Stack:
    ''' Stack ADT'''
    
    def __init__(self):
        '''Create empty stack'''
        self.data = []
        '''Precedence for operators'''
        self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3} 
    
    def isEmpty(self):
        '''Check if a stack is empty'''
        return len(self.data) == 0
    
    def push(self, e):
        '''Add new item to top of stack'''
        self.data.append(e)
        
    def pop(self):
        '''Return top element of the stack, while removing it'''
        if self.isEmpty():
            raise Empty('Stack is empty')
        return self.data.pop()
        
    def peek(self):
        '''Return top element of the stack, without removing'''
        if self.isEmpty():
            raise Empty('Stack is empty')
        return self.data[-1] 
    
    def __len__(self):
        '''Return length of stack'''
        return len(self.data)

    def notGreater(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            return True if a  <= b else False
        except KeyError:
            return False

def cleanString(string):
    '''Standardise delimiters, and remove all spaces'''
    output = ''
    for c in string:
        if c in '[{':
            c = '('
        elif c in ']}':
            c = ')'
        elif c == ' ':
            c = ''
        elif c == '–':
            c = '-'
        output += c

    for c in output:
        if not (str.isalpha(c) or c in '^+-–*/()'):
            print("ERROR: Invalid character in string:'{}' \nRefer to README.md.". format(c))
            return -1

    return output

def reverseString(string):
    '''Reverse a string to read it RIGHT to LEFT'''
    storageStack = Stack() # temporary Stack to reverse the string
    reversed_string = '' # store the reverse string
    
    for c in string:
        '''Invert all brackets'''
        if c == '(':
            c = ')'
        elif c == ')':
            c = '('
        storageStack.push(c)
    '''Invert the expression to read RIGHT to LEFT'''
    
    
    while not storageStack.isEmpty():
        reversed_string += storageStack.pop()

    return reversed_string

def in_post(in_string):
    '''Function for converting INFIX to POSTFIX'''
    operandStack = Stack()
    postfix = []

    '''Read LEFT to RIGHT'''
    for c in in_string:

        if str.isalpha(c):
            '''Insert OPERATORS into postfix'''
            postfix.append(c)

        elif c == '(':
            '''Push all ( into stack'''
            operandStack.push(c)

        elif c == ')':
            '''Pop all OPERATORS in stack until a corresponding ( is met'''
            
            while (not operandStack.isEmpty() and operandStack.peek() != '('):
                '''Make sure that stack is not empty + next operator is not a ('''
                c = operandStack.pop()
                postfix.append(c)
            
            if (not operandStack.isEmpty() and operandStack.peek() != '('):
                return -1
            else:
                operandStack.pop()

        else: #operator
            while (not operandStack.isEmpty() and operandStack.notGreater(c)):
                postfix.append(operandStack.pop())
            operandStack.push(c)

    while not operandStack.isEmpty():
        postfix.append(operandStack.pop())

    postfix = ''.join(postfix) # Convert into string
    
    return postfix


def in_pre(in_string):
    '''Function for converting INFIX to PREFIX'''
    
    prefixStack = Stack()
    prefix = ''
    
    reversed_string = reverseString(in_string)
    '''Convert inversed string into 'postfix' notation'''
    postfix = in_post(reversed_string)

    '''Convert 'postfix' into prefix'''
    for c in postfix:
        '''Invert the expression to read RIGHT to LEFT'''
        prefixStack.push(c)
    while not prefixStack.isEmpty():
        prefix += prefixStack.pop()

    return prefix


def pre_in(pre_string):
    '''Function for converting PREFIX to INFIX'''
    
    '''Reverse the string to read from RIGHT to LEFT'''
    reversed_string = reverseString(pre_string)

    operatorStack = Stack()
    temp = ''
    infix = ''
    for c in reversed_string:
        if str.isalpha(c):
            operatorStack.push(c)
        else:
            pop1 = operatorStack.pop()
            pop2 = operatorStack.pop()
            temp = '(' + pop1 + c + pop2 + ')'
            operatorStack.push(temp)

    infix = '' + operatorStack.pop() 

    return infix

def post_in(post_string):
    '''Function for converting POSTFIX to INFIX'''

    operatorStack = Stack()
    '''Read string LEFT to RIGHT'''
    for c in post_string:
        if str.isalpha(c):
            operatorStack.push(c)
        else:
            pop1 = operatorStack.pop()
            pop2 = operatorStack.pop()
            temp = '(' + pop2 + c + pop1 + ')' 
            operatorStack.push(temp)

    infix = '' + operatorStack.pop() 

    return infix
    
def pre_post(pre_string):
    '''Function for converting PREFIX to POSTFIX'''

    infix = pre_in(pre_string)
    postfix = in_post(infix)

    return postfix

def post_pre(post_string):
    '''Function for converting POSTFIX to PREFIX'''

    infix = post_in(post_string)
    prefix = in_pre(infix)

    return prefix