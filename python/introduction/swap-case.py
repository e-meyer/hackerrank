# using swapcase method:

def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

# not using string methods

#    new_str = []
#    
#    for i in s:
#        if i.isupper():
#            new_str.append(i.lower())
#        elif i.islower():
#            new_str.append(i.upper())
#        else:
#            new_str.append(i)
#    
#        print(''.join(new_str))