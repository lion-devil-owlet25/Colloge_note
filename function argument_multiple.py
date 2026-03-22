'''# function with variable-length keyword arguments
def marks(**kwargs):
    
    for sub in kwargs:
        # get argument name
        sub_name = sub
        # get argument value
        sub_marks = kwargs[sub]
        print(sub_name, "=", sub_marks,end=' ')

# pass multiple keyword arguments
marks(math=56, english=61)
print()
marks(math=56, english=61, science=73)
print()
marks(math=56, english=61, science=73, history=45)

#A default value can be set for any number of
#arguments in a function. However, if we have a
#default argument, we must likewise have default
#values for all the arguments to their right.
#Non-default arguments, in other words, cannot
#be followed by default arguments.

def function(b, c, a = 24):
    print('Values are:')
    print(a)
    print(b)
    print(c)

function(10, 4,'soumyadeep')
'''
#However, we must remember that the keyword
#arguments must always come after the positional
#arguments. There will be issues if a positional
#argument is used after the keyword arguments.

def fruits(p,a,b):
    print('We have', a+ ',', b+ ' and', p+ ' at our store.')
fruits('pineapple', 'apple',b = 'banana')





    
