import time


def is_palidrome(num):
    """Return a boolean representing if the number is a palidrome"""
    num_str = str(num)
    
    return False
    
#Test if is_plaindrome() works
print(is_palidrome(5))
print(is_palidrome(10101))
print(is_palidrome(2002))
print(is_palidrome(524251))

start_time = time.time()
#Loop through three digit numbers

    
end_time = time.time()
print("Program took " + str(end_time - start_time) + " seconds to run")
