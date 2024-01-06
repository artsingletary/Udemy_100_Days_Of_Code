#Unlimited positional arguments


def add(*args): 
    print(args)
    print(type(args))

    sum = 0
    for n in args: 
       sum += n
    print (sum)



add(1,2,3,4,5)