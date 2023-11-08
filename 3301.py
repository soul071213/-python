# a=int(input())
# count=0
# while(a>9):
#     if(a>=50000):
#         a=a-50000
#         count=count+1
#     elif(a>=10000):
#         a=a-10000
#         count=count+1
#     elif(a>=5000):
#         a=a-5000
#         count=count+1
#     elif(a>=1000):
#         a=a-1000
#         count=count+1
#     elif(a>=500):
#         a=a-500
#         count=count+1
#     elif(a>=100):
#         a=a-100
#         count=count+1
#     elif(a>=50):
#         a=a-50
#         count=count+1
#     elif(a>=10):
#         a=a-10
#         count=count+1
    
# print(count)
    
a = int(input()) # 변수 a에 거슬러 줘야 할 돈을 입력받아 저장한다.
count = 0		 # 거스름돈 갯수를 저장할 count 변수를 초기화 한다. 

 				 # 거스름돈 단위를 큰 수 부터 i에 불러온다
for i in [50000, 10000, 5000, 1000, 500, 100, 50, 10]:
    if a // i != 0 : 	# 거슬러줄 돈이 i로 나뉘면 i로 거슬러 줄 수 있다.
        count += a // i # 거스름돈 갯수에 i로 거슬러 준 갯수를 기존 count변수에 더해준다.
        a = a % i		# i로 거슬러 주고난 나머지를 변수 a에 저장한다. 

print(count)			# 거스름돈 갯수를 출력한다.
