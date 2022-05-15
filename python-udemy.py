# tuple unpacking with python functions 
from sqlalchemy import false, true


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

#function calling another function 

# shuffle list 
def shuffle_list():
    
    import random
    num_list = ['','O','']
    random.shuffle(num_list)
    return num_list

# get user preference
def get_user_choice():
    user_choice =''
    while (user_choice not in ['0','1','2']):
        user_choice = input("Enter a number between 0 and 2: ")
    return user_choice  

# compare shuffle list with user preference
def compare_user_choice(list,choice):
    if (list[int(choice)]=='O'):
        return "Success"
    return "Better luck next time"



new_list = shuffle_list()
choice = get_user_choice()
result = compare_user_choice(new_list,choice)
print(result)


#define lesser of two events

def lesser_events(a,b):
    if(int(a)%2== 0 and a<b):
        return a
    elif(int(b)%2 ==0 and b<a):
        return b    
    else:
        return "Both numbers are not even"

print(lesser_events(20,89))




#*ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin 
# with same letter
#animal_crackers('Levelheaded Llama') --> True
#animal_crackers('Crazy Kangaroo') --> False 

def animal_crackers(two_word):
   second_occur = two_word[two_word.find(" ")+1]
   first_occur = two_word[0]
   if first_occur == second_occur:
       return True
   return False


animal_crackers("Priyanga Panni")

