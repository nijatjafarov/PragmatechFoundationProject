# Link -> https://www.hackerrank.com/challenges/text-wrap/problem

wrapped_str = []
def wrap(string, max_width):
    for divider in range(max_width, len(string), max_width):
        wrapped_str.append(string[divider-max_width:divider])
    wrapped_str.append(string[-(len(string)%max_width):])
    return "\n".join(wrapped_str)

string, max_width = input(), int(input())
result = wrap(string, max_width)
print(result)