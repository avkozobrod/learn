from decimal import Decimal

def perimetr_square(a):
    print("P = ",4*float(a))
#perimetr_square(10)

def area_square(a):
    print("S = ",float(a)**2)
#area_square(15)

def perimetr_and_area_rectangle(a,b):
    print("S = ",float(a)*float(b))
    print("P = ", 2*(float(a)+float(b)))
#perimetr_area_rectangle(23,67)

def diametr_circle(d):
    pi='3.14'
    print("L = ",Decimal(pi)*Decimal(str(d)))
#diametr_circle(3.567)

def volume_and_area_cube(a):
    print("V = ",float(a)**3)
    print("S = ",6*float(a)**2)
#volume_and_area_cube(10)

def volume_and_area_rectangle_prism(a,b,c):
    print("V = ", float(a)*float(b)*float(c))
    print("S = ", 2 * (float(a)*float(b)+float(b)*float(c)+float(a)*float(c)))
#volume_and_area_rectangle_prism(12,3,8)

def circumference_and_area_circle(R):
    pi='3.14'
    print("L = ",2*Decimal(pi)*Decimal(str(R)))
    print("S = ",Decimal(pi)*Decimal(str(R))**2)
#circumference_and_area_circle(12.91)

def average(a,b):
    print((float(a)+float(b))/2)
#average(3.15,3.57)

def geometric_mean(a,b):
    print((abs(float(a)*float(b))**0.5))
#geometric_mean(-2,8.0)

def sum_difference_product_and_quotient(a,b):
    if a!=0 and b!=0:
        print(float(a)**2+float(b)**2)
        print(float(a)**2-float(b)**2)
        print(float(a)**2*float(b)**2)
        print(float(a)**2/float(b)**2)
#sum_difference_product_and_quotient(0.0,2)

