stack_size=5
top=-1
list=[None]*stack_size

def push(a):

    if not isFull(): 
        global top
        top=top+1
        list[top]=a 
    else:
        pass
def pop():
    if not isEmpty():
        global top
        top=top-1
        return list[top+1] 
    else:
        pass
def isEmpty():
    if(top==-1):
        return True
    else:
        return False
def isFull():
    if(top==stack_size-1):
        return True
    else:
        return False
def peek():
    if not isEmpty():
        return list[top]
    else:
        pass
    

push(1)
push(2)
push(3)
push(4)
push(5)
push(6)

print(peek())
print(pop())
print(pop())
print(peek())