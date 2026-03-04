def format_name(f_name,l_name):
    f=f_name.title()
    l=l_name.title()
    return f"{f} {l}"

print(format_name("punEEth","RAjashekar"))

def function_1(text):
    return text + text

def function_2(text):
    return text*2

output=function_2(function_1("puneeth"))
print(output)