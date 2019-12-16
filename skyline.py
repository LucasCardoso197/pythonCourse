def myfunc(s):
    result = ''
    odd = s[0::2]
    even = s[1::2]
    odd = odd.lower()
    even = even.upper()

    for i, _ in enumerate(even):
        result += odd[i]
        result += even[i]
    if len(s)%2 != 0:
        result += odd[i+1]
    
    return result

s = myfunc('qwertYUIOP')
print(s)