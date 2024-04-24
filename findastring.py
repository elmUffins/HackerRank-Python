#Find a String
def count_substring(string, sub_string):
    x = 0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i + len(sub_string)] == sub_string:
            x += 1
    return x

string = input().strip()
sub_string = input().strip()

count = count_substring(string, sub_string)
print(count)
