def first_meat_orders(num_of_orders, orders, size):
    result = []
    
    for i in range(0, num_of_orders-size+1):
        screen_orders = orders[i:i+size]
        meat_order_found = False
        
        for order in screen_orders:
            if order < 0:  # Checking for meat-based pizza order
                result.append(order)
                meat_order_found = True
                break

        
        if not meat_order_found:
            result.append(0)
        meat_order_found = False
    
    return result

# Input parsing
num_of_orders = int(input())
orders = list(map(int, input().split()))
size = int(input())

# Calling the function and printing the result
output = first_meat_orders(num_of_orders, orders, size)
print(*output)

# sample input
# 6
# -11 -2 19 37 64 -18
# 3
