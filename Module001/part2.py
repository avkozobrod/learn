def distance(L):
    print(int(L)//100)
#distance(1246)

def wieght(M):
    print(int(M)//1000)
#wieght(34)

def file_size(a):
    print(int(a)//1024)
#file_size(2340)

def number_segments(A,B):
    print(A//B)
#number_segments(56,15)

def residual(A,B):
    print(A%B)
#residual(36,9)
def two_digit_number(a):
    print(a//10)
    print(a%10)
#two_digit_number(34)

def two_digit_number_sum_and_product(a):
    print((a//10)+(a%10))
    print((a//10)*(a%10))
#two_digit_number_sum_and_product(27)

def two_digit_reverse(a):
    #print(int(str(a%10)+str(a//10)))
    print((a%10)*10+(a//10))
#two_digit_reverse(63)

def three_digit_nuber_first_digit(a):
    print(a//100)
#three_digit_nuber_first_digit(623)

def three_digit_nuber_last_and_middle_digit(a):
    print(a%10)
    print((a//10)%10)
#three_digit_nuber_last_and_middle_digit(743)