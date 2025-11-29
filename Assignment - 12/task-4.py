import math

# Function and derivative
def f(x):
    return 2*(x**3) + 4*x + 5

def df(x):
    return 6*(x**2) + 4   # derivative of 2x^3 + 4x + 5

# Gradient Descent Settings
learning_rate = 0.0001
x = 0.0                      # starting point
max_iters = 200000
grad_clip = 1000             # clip large gradients
x_clip_min, x_clip_max = -10, 10   # keep x within safe range

for i in range(max_iters):
    grad = df(x)

    # Clip gradient to avoid overflow
    grad = max(min(grad, grad_clip), -grad_clip)

    # Update rule
    x = x - learning_rate * grad

    # Clip x to prevent it from growing too large
    x = max(min(x, x_clip_max), x_clip_min)

# Final output
print("Minimum occurs at x =", x)
print("f(x) =", f(x))