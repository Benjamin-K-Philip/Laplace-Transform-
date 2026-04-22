# Laplace Transform

## Decription 
The concepts of Laplace Transform and Inverse Laplace Transform is implemented by using both Python and the SymPy package where the transformation and its inverse transformation of algebraic and trigonometric expressions are computed symbolically. The program uses the Matplotlib tool to plot these transformations numerically in the time domain.

---

## Description of the selected problems <br>
Following are the Problems selected:- <br>

**Q1.) To solve the following Laplace Transform problems:** <br>
**(a) *x*<sup>5</sup> *e*<sup>-2*x*</sup> <br>
(b) (1 - *x*<sup>2</sup>) *e*<sup>-*x*</sup> <br>
(c) *e*<sup>3*x*</sup> cos 2*x* <br>**

**Q2.) To solve the following Inverse Laplace transform problems:** <br>
**(a) $\frac{6}{(p+2)^2 + 9}$**

**(b) $\frac{12}{(p+3)^4}$**

**(c) $\frac{p+3}{p^2 + 2p + 5}$**


The above selected problems are from the **textbook Differential Equations With Applications and Historical Notes, from Chapter 9: Laplace Transforms, Section 50. The Laplace Transform** is a mathematical tool that shifts functions from the time domain (**_variable x_**) into the frequency domain (**_variable p_**). It is primarily used to simplify the process of solving linear differential equations by turning calculus into algebra. Following are the description for the above problems:

➤ **Distinguishing and Classification:** <br>
   - **Laplace Problems (Question 1):** These are identified by functions of **_x_** (like _x_<sup>*5*</sup> or cos 2_x_) being multiplied by an exponential **_e<sup>ax</sup>_**. They are classified as Frequency Shifting problems.

   - **Inverse Laplace Problems (Question 2):** These are identified by rational functions of **_p_**. They are classified based on their denominators—specifically those requiring Completing the Square or recognizing Shifted Power/Trig forms.

➤ **Use of Laplace Transforms (Question 1):** Converts complex differentiation and integration into simple algebraic multiplication and division. Used to model and analyze the behavior of electrical circuits and mechanical vibrations.

➤ **Use of Inverse Laplace Transforms (Question 2):** Translates the algebraic solution found in the **_p-domain_** back into a readable **_x-domain_** format. Determines how a physical system will actually react over time when given a specific input or "impulse."

---

## Procedure/Method used
The Laplace Transform is defined as: <br>
**$L[f(x)] = \int_0^{\infty} e^{-px} f(x) \, dx = F(p)$** 

Following are the procedures that describes the Laplace Transforms:

➤ **Procedure for Laplace Transforms:**
The goal is to transform a function of time **_f(x)_** into a function of the complex frequency **_F(p)_**.

   1. **Linearity Check:** If the function is a sum, such as **_f(x) = g(x) + h(x)_**, split it into individual parts i.e. **_L{g(x)} + L{h(x)}_**.

   2. **Identify the Core Function:** Looking for the basic trigonometric (sin, cos), hyperbolic, or power (**_x<sup>n</sup>_**) function within the expression.

   3. **Apply the First Shifting Theorem:** If the function is multiplied by **_e<sup>ax</sup>_**, first we find the Laplace of the core function and then replace every **_p_** with **_(p - a)_**. <br>
   **Formula:** **$L\{e^{ax}f(x)\} = F(p - a)$**

   4. **Using Simple Transform Pairs:** Using the Simple Transform Pairs Table to convert the core function.
   <img width="362" height="533" alt="image" src="https://github.com/user-attachments/assets/4fdc0286-f0f3-4b08-93c5-82642b175017" />
<br>
   5. **Simplification:** Combining the algebraic fractions into their simplest form.

<br>

➤ **Procedure for Inverse Laplace Transforms:**
The goal is to take a frequency domain function **_F(p)_** and return it to the time domain **_f(x)_**

   1. **Denominator Analysis:** If the denominator is a quadratic that cannot be factored (like **$p^2 + 2p + 5$**), then use Completing the Square to get it into the form **$(p + a)^2 + b^2$**. Using Partial Fraction Decomposition to break complex fractions into simpler terms.

  
