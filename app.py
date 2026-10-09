def is_even(*args):
    for num in args :
        if num % 2 == 0 :
            print(f'{num} is even and more than 10.')  
        else :
            print(f"{num} isn't a even number.")     

is_even( 10 , 1 , 20 )
