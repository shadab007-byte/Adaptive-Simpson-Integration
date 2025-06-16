import numpy as np

# Define the function f(x)
def f(x):
    term1 = 10 * np.exp(-50 * np.abs(x))
    term2 = -0.01 / ((x - 0.5)**2 + 0.001)
    term3 = 5 * np.sin(5 * x)
    return term1 + term2 + term3

# Two-panel Simpson's rule (S)
def simpson_two_panel(f, a, b):
    h = b - a
    mid = (a + b) / 2
    return h / 6 * (f(a) + 4 * f(mid) + f(b))

# Four-panel Simpson's rule (S(2))
def simpson_four_panel(f, a, b):
    h = (b - a) / 2
    x0 = a
    x1 = a + h / 2
    x2 = (a + b) / 2
    x3 = b - h / 2
    x4 = b
    return h / 6 * (f(x0) + 4 * f(x1) + 2 * f(x2) + 4 * f(x3) + f(x4))

# Adaptive Simpson's Method
def adaptive_simpson(f, a, b, tol, max_depth=50, depth=0):
    S = simpson_two_panel(f, a, b)  # Two-panel Simpson's estimate
    S2 = simpson_four_panel(f, a, b)  # Four-panel Simpson's estimate
    error_estimate = abs(S2 - S) / 15  # Estimate of error using key result

    if error_estimate <= tol * (b - a):  # Check if tolerance is satisfied
        return S2  # Accept the four-panel result
    elif depth >= max_depth:  # Safety to prevent infinite recursion
        return S2  # Return current estimate if depth exceeded
    else:
        # Subdivide and apply method to each subinterval
        mid = (a + b) / 2
        left_result = adaptive_simpson(f, a, mid, tol / 2, max_depth, depth + 1)
        right_result = adaptive_simpson(f, mid, b, tol / 2, max_depth, depth + 1)
        return left_result + right_result

# Integration limits
a, b = -1, 1

# List of tolerances
tolerances = [10**(-i) for i in range(2, 8)]

# Perform integration for each tolerance
results = []
for tol in tolerances:
    result = adaptive_simpson(f, a, b, tol)
    results.append((tol, result))

# Print the results
print(f"{'Tolerance':<12} {'Integral':<20}")
for tol, integral in results:
    print(f"{tol:<12.1e} {integral:<20.10f}")
