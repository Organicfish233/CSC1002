import math
nums = []
def gen_wrong(n):
    nums.append(1)
    nums.append(0)
    counter = 1
    while True:
        if (counter>n+1):
            return
        yield nums[counter]
        if counter == 1:
            nums.append(1)
        else:
            ele = counter*(nums[counter]+nums[counter-1])
            nums.append(ele)
        counter += 1


f = gen_wrong(100)
formula = [1]
while True:
    try:
        ele = next(f)
        formula.append(ele)
    except:
        break
def hat_check(n):
    def combination(a,b):
        return (math.factorial(a)/(math.factorial(b)*math.factorial(a-b)))


    def calculate(p_n):
        result = 0
        for i in range(0,p_n+1):
            temp = (p_n-i)*formula[i]*int(combination(p_n,i))
            result += temp
        return result/(math.factorial(p_n))
    return calculate(n)

for i in range(1,10):
    print(hat_check(i))

