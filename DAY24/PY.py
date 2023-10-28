def error_print(opt):
    print(f"There is no option[{opt}]")

def find_divisor(num):
    divisor={1}
    for i in range(2,num+1):
        if num%i==0:
            divisor.add(i)
    return divisor
def find_GCD(num1,num2):
    d1=find_divisor(num1)
    d2=find_divisor(num2)
    return max(d1&d2)
def find_LCM(num1,num2):
    d1=find_divisor(num1)
    d2=find_divisor(num2)
    return max(d1&d2)*(num1/max(d1&d2))*(num2/max(d1&d2))
def calculate(num1,num2,opt):
    if opt==1:
        print(f"GCD is {find_GCD(num1,num2)}")
    elif opt==2:
        print(f"LCM is {find_LCM(num1,num2)}")
    else:
        error_print(opt)
if __name__=="__main__":
    print("==============================================================================================")
    num1=input("[first number]+[number]:")
    num2=input("[second number]+[enter]:")
    opt=input("(1)GCD or (2 LCM)+[enter]:")

    calculate(int(num1),int(num2),int(opt))