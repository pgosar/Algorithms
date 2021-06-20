#newton's method does square roots
#constantly iterates until the answer is below the threshold for correctness
def newton(x):
    n = x
    while True:
        
        root = 0.5 * (x+ (n/x))
        if abs(root-x) < 0.000000001:
            break
        
        x = root
        
    return root
    

print(newton(43928.34434839))