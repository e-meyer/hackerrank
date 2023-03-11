def count_substring(string, sub_string):
    total_times = 0
    for i in range(len(string)):
        aux_string = string[i:i+len(sub_string)]
        if sub_string == aux_string:
            total_times += 1
        # or
        # for i in range(len(string)):
        # if sub_string == string[i:i+len(sub_string)]:
        #     total_times += 1
     
    return total_times

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)