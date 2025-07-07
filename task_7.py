
def digit_root(num):
    sum_number = sum(int(d) for d in str(num))
    if sum_number < 10:
        return sum_number
    else:
        return digit_root(sum_number)


print(digit_root(4851))
print(digit_root(97569))
print(digit_root(889987))
