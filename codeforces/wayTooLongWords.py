_ = [print(s[0] + str(len(s) - 2) + s[-1]) if len(s) > 10 else print(s) for _ in range(int(input())) for s in [input()]]
