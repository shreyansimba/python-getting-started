# tuple unpacking with python functions 
stock_prices = [('AAPl',200),('MSFT',400),('AAPl',300)]

for ticker,prices in stock_prices :
    print (ticker)
    print (prices)

# employee of the year 
emp_hours = [('Raj',200),('Priya',1000),('Shreya',900),('Simba',10)]

def get_emp_of_the_year(emp_hours): 
    hours_max = 0
    emp_of_the_year=""; 
    for emp,hours in emp_hours:
        if hours> hours_max:
            hours_max = hours
            emp_of_the_year = emp
    
    print ("Employee of the year is {} with {} hours".format(emp_of_the_year,hours_max))

get_emp_of_the_year(emp_hours)


