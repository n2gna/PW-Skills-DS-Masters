##Q1) Write a program to accept percentage from the user and display the grade according to the following criteria

user_marks = int(input('Please enter your marks without the % sign '))

if user_marks > 90:
    grade = 'A'
elif user_marks > 80:
    grade = 'B'
elif user_marks > 60:
    grade = 'C'
else:
    grade = 'D'
    
print(f'Your grade is {grade}.') 


##Q2) Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria

cost_price = int(input('Please enter the cost price of your bike without any symbols '))

if cost_price > 100000:
    tax = cost_price *  0.15
elif cost_price > 50000:
    tax = cost_price * .10
else:
    tax = cost_price * .05
    
print(f'The road tax to be paid by you is Rs. {int(tax)}')

##Q3) Accept any city from the user and display monumnets of that city

city = input('Please enter a city ').title()

if city == 'Delhi':
    print(f'The famous monument of {city} is Red Fort.')
elif city == 'Agra':
    print(f'The famous monument of {city} is Taj Mahal')
elif city == 'Jaipur':
    print(f'The famous monument of {city} is Jal Mahal.')
else:
    print('Please enter a different city')
    
       
    


##Q4) Check how many times a give number can be divided by 3 before it is less than or equal to 10

user_num = float(input('Please enter a number '))

counter = 0

while (user_num > 10):
    user_num = user_num/3
    counter+=1
    
if counter == 1 or counter == 0 :   
    print(f'The number {user_num} can be divided by 3 for {counter} time before it is less than or equal to 10') 
else:
    print(f'The number {user_num} can be divided by 3 for {counter} times before it is less than or equal to 10') 


##Q5) Why and when to use while loop in Python give a detail description with example

'''While loop is used in Python to repeat a block of code until a given condition becomes False.
The following example shows that 1 is added to n until n becomes more than 10'''

n = 1
while n <= 10:
    print(n)
    n += 1
    
    


##Q6) Use nested while loop to print 3 different pattern
#first pattern

n = 5
x = 1
while n > 0:
    y = x
    while y > 0:
        print('*', end='')
        y-=1
        
    x+=1
    n-=1
    print('\r')


#second pattern

n = 5

while n > 0:
    i = n
    while i > 0:
        print('*', end='')
        i-=1

    n-=1
    print('\r')
    

#third pattern

n = 5
i = 0
y = 2*n-1 

while n > 0:
    j = i
    while j > 0:
        print(' ', end='')
        j-=1
    while y > 0:  
        print('*', end='')
        y-=1
    
    i+=1
    n-=1
    y = 2*n-1 
    
    print('\r')
    

##Q7and8) Reverse a while loop to display numbers from 10 to 1 

n = 10
while n > 0:
    print(n)
    n -= 1
#Q7 and Q8 are the same.    
    
