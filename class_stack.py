class ii:
    def __init__(self):
        self.max_size=5
        self.arr1=[None] * self.max_size
        self.top=-1
class stack(ii):
    def __init__(self,ip):
        super().__init__()
        self.ip=ip
    def push(self):
       if not self.isFull():
            self.top+=1
            self.arr1[self.top]=self.ip
    def isEmpty(self):
        if(self.top==-1):
            return True
        return False
    def isFull(self):
        if(self.top==self.max_size-1):
            return True
        return False
    def pop(self):
       if not self.isEmpty():
            self.top-=1
            return self.arr1[self.top+1]
    def peak(self):
       if not self.isEmpty():
            return self.arr1[self.top]

ii()
while(1):
    print("1은 push 2는 pop 3은 peak")
    k=int(input())
    if(k==1):
        print("push 실행")
        ip=int(input())
        st1=stack(ip)
        st1.push()

    elif(k==2):
        print("pop 실행")
        print(st1.pop()) 

    elif(k==3):
        print("peak 실행")
        print(st1.peak())

    else:
         print("끝")
         break

