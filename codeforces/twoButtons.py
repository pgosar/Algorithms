
buttons = [int(i) for i in input().split()]
ans = 0
while buttons[0] != buttons[1]:
    if buttons[1] > buttons[0]:
        if buttons[1] % 2 == 0:
            buttons[1] //= 2
            ans += 1
        else:
            buttons[1] += 1
            ans += 1

    elif buttons[1] < buttons[0]:
        buttons[1] += 1
        ans += 1
print(ans)
