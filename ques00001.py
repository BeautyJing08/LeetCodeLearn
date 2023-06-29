'''
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''
# 菁的第一個 Leet Code 題目就遇到困難惹哈哈哈哈哈

# array = [2,7,11,15]
# answer = 9

# print(array[0])
# print(array[1])
# print(array[0]+array[1])
##############################################

# arrayNum = len(array) # 這個array當中有多少個element
# print(arrayNum) # 印出共有多少個element
# print(range(arrayNum)) # arrayNum = 4 , range(0,4) = [0,1,2,3]
# print(list(range(arrayNum))) #列出[0,1,2,3]
#
# listarray = list(range(arrayNum))
# print(listarray)

####

# randomitem = random.sample(listarray,2)
# print(randomitem)

##############################################
import random
def findrandomitem(array):
    randomitemArray= random.sample(array,2)
    return randomitemArray

array = [2,7,11,15]
answer = 9

arrayNum = len(array) # 這個array當中有多少個element
listarray = list(range(arrayNum))
# ran = findrandomitem(listarray)
# print(ran)

k=0
def caculateAnswer(array,listarray,k):
    if k==0:
        print(f"LeedCode Question:")
        print(f"initarray= {array}")
        print(f"listarray= {listarray}")
    k += 1
    print(f"=========it's {k} times=========")

    randomitem = findrandomitem(listarray)
    print(randomitem)
    num1 = array[randomitem[0]]
    num2 = array[randomitem[1]]
    # print(num1,num2)
    if num1+num2 == answer:
        print(f"cuz num1 + num2 = answer = {answer}, stop method")
        print(f"answer= {randomitem}")
        print(f"num1= {num1}, radomitem= {randomitem[0]}")
        print(f"num2= {num2}, radomitem= {randomitem[1]}")
    else:
        caculateAnswer(array,listarray,k) #若沒有找到解答，那就重新random找答案


caculateAnswer(array,listarray,k)


