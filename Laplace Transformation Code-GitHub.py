import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# symbols
x, p = sp.symbols('x p', real=True, positive=True)

# --------------------------------------------------
# Simple plotting function
# --------------------------------------------------
def plot_graph(expr, title):
    f = sp.lambdify(x, expr, modules=["numpy"])
    x_vals = np.linspace(0, 5, 400)
    y_vals = f(x_vals)

    plt.figure(figsize=(8, 4))
    plt.plot(x_vals, y_vals, color="blue", linewidth=2)
    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.show()

# --------------------------------------------------
# Laplace transform questions
# --------------------------------------------------
def laplace_problems():
    print("\n--- Laplace Transforms ---")

    # 1(a)
    q1 = x**5 * sp.exp(-2*x)
    a1 = sp.laplace_transform(q1, x, p, noconds=True)
    print("\n1(a) Question: x^5 * e^(-2x)")
    print("Solution:", a1)
    plot_graph(q1, "1(a) y = x^5 e^(-2x)")

    # 1(b)
    q2 = (1 - x**2) * sp.exp(-x)
    a2 = sp.laplace_transform(q2, x, p, noconds=True)
    print("\n1(b) Question: (1 - x^2) * e^(-x)")
    print("Solution:", a2)
    plot_graph(q2, "1(b) y = (1 - x^2)e^(-x)")

    # 1(c)
    q3 = sp.exp(3*x) * sp.cos(2*x)
    a3 = sp.laplace_transform(q3, x, p, noconds=True)
    print("\n1(c) Question: e^(3x) cos(2x)")
    print("Solution:", a3)
    plot_graph(q3, "1(c) y = e^(3x) cos(2x)")

# --------------------------------------------------
# Inverse Laplace transform questions
# --------------------------------------------------
def inverse_laplace_problems():
    print("\n--- Inverse Laplace Transforms ---")

    # 2(a)
    q1 = 6 / ((p + 2)**2 + 9)
    a1 = sp.inverse_laplace_transform(q1, p, x).replace(sp.Heaviside(x), 1)
    print("\n2(a) Question: 6 / ((p + 2)^2 + 9)")
    print("Solution:", a1)
    plot_graph(a1, "2(a) y = 2e^(-2x) sin(3x)")

    # 2(b)
    q2 = 12 / (p + 3)**4
    a2 = sp.inverse_laplace_transform(q2, p, x).replace(sp.Heaviside(x), 1)
    print("\n2(b) Question: 12 / (p + 3)^4")
    print("Solution:", a2)
    plot_graph(a2, "2(b) y = 2x^3 e^(-3x)")

    # 2(c)
    q3 = (p + 3) / (p**2 + 2*p + 5)
    a3 = sp.inverse_laplace_transform(q3, p, x).replace(sp.Heaviside(x), 1)
    print("\n2(c) Question: (p + 3) / (p^2 + 2p + 5)")
    print("Solution:", a3)
    plot_graph(a3, "2(c) y = e^(-x)cos(2x) + e^(-x)sin(2x)")

# --------------------------------------------------
# Main program
# --------------------------------------------------
def main():
    while True:
        print("\n" + "="*40)
        print("LAPLACE TRANSFORM TOOL")
        print("="*40)
        
        print("""  
Choice 1: 
To solve the following Laplace Transform problems :-
(a) Question: x^5 e^{-2x} 
(b) Question: (1 - x^2) e^{-x}
(c) Question: e^{3x} cos 2x 
""") #print statement for choice 1 
        
        print("""
Choice 2:
To solve the following Inverse Laplace transform problems :- 
(a) Question: {6}/{(p + 2)^2 + 9} 
(b) Question: {12}/{(p + 3)^4} 
(c) Question: {p + 3}/{p^2 + 2p + 5} 
""")#print statement for choice 2
        
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            laplace_problems()
        elif choice == "2":
            inverse_laplace_problems()
        elif choice == "3":
            print("Thank you. Terminating program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()