def is_even(*args):
    name = 'justice!'
    for num in args :
        if num % 2 == 0 :
            print(f'{num} is even and more than 10.')  
        else :
            print(f"{num} isn't a even number.")     
    for justice in range(1 , 10):
        print(name)
is_even( 10 , 1 , 20 )
