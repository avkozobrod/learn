def perimetr_square(a):
    print("P = ",4*a)
#perimetr_square(10.0)

def area_square(a):
    print("S = ",a**2)
#area_square(15.0)

def perimetr_and_area_rectangle(a,b):
    print("S = ",a*b)
    print("P = ", 2*(a+b))
#perimetr_area_rectangle(23.0,67.0)

def diametr_circle(d):
    pi=3.14
    print("L = ",pi*d)
#diametr_circle(3.567)

def volume_and_area_cube(a):
    print("V = ",a**3)
    print("S = ",6*a**2)
#volume_and_area_cube(10.0)

def volume_and_area_rectangle_prism(a,b,c):
    print("V = ", a*b*c)
    print("S = ", 2 * (a*b+b*c+a*c))
#volume_and_area_rectangle_prism(12.1,3.1,8.1)

def circumference_and_area_circle(R):
    pi=3.14
    print("L = ",2*pi*R)
    print("S = ",pi*R**2)
#circumference_and_area_circle(12.91)

def average(a,b):
    print((a+b)/2)
#average(3.15,3.57)

def geometric_mean(a,b):
    print((a*b)**0.5)
#geometric_mean(2.0,8.0)

def sum_difference_product_and_quotient(a,b):
    print(a**2+b**2)
    print(a**2-b**2)
    print(a**2*b**2)
    print(a**2/b**2)
#sum_difference_product_and_quotient(5.1,2.2)
