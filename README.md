# Adaptive Simpson's Rule for Numerical Integration

This Python script implements **Adaptive Simpson's Rule** to evaluate the integral of a complex function with sharp features and oscillations.

## 🧠 What It Does

- Applies Simpson’s Rule on two-panel and four-panel intervals
- Estimates integration error using Richardson extrapolation
- Recursively subdivides the interval if error exceeds tolerance
- Computes the integral for multiple tolerance values

## 📌 Function Being Integrated

\[
f(x) = 10 e^{-50|x|} - \frac{0.01}{(x - 0.5)^2 + 0.001} + 5\sin(5x)
\]

This function has a sharp spike near `x = 0.5` and rapid oscillations, making it ideal for testing adaptive quadrature.



