# Laplace Transform

## Decription 
The concepts of Laplace Transform and Inverse Laplace Transform is implemented by using both Python and the SymPy package where the transformation and its inverse transformation of algebraic and trigonometric expressions are computed symbolically. The program uses the Matplotlib tool to plot these transformations numerically in the time domain.

---

## Description of the selected problems <br>
Following are the Problems selected:- <br>

**Q1.) To solve the following Laplace Transform problems:** <br>
**(a)** **$x^5 \ e^{-2x}$** <br>
**(b)** **$(1 - x^2) \ e^{x}$** <br>
**(c)** **$e^{3x} \cos 2x$** <br>

**Q2.) To solve the following Inverse Laplace transform problems:** <br>
**(a) $\frac{6}{(p+2)^2 + 9}$**

**(b) $\frac{12}{(p+3)^4}$**

**(c) $\frac{p+3}{p^2 + 2p + 5}$**


The above selected problems are from the **textbook Differential Equations With Applications and Historical Notes, from Chapter 9: Laplace Transforms, Section 50. The Laplace Transform** is a mathematical tool that shifts functions from the time domain ($variable \ x$) into the frequency domain ($variable \ p$). It is primarily used to simplify the process of solving linear differential equations by turning calculus into algebra. Following are the description for the above problems:

➤ **Distinguishing and Classification:** <br>
   - **Laplace Problems (Question 1):** These are identified by functions of **$x$** (like $x$<sup>*5*</sup> or **$\cos 2x$**) being multiplied by an exponential **$e^{ax}$**. They are classified as Frequency Shifting problems.

   - **Inverse Laplace Problems (Question 2):** These are identified by rational functions of $p$. They are classified based on their denominators—specifically those requiring Completing the Square or recognizing Shifted Power/Trig forms.

➤ **Use of Laplace Transforms (Question 1):** Converts complex differentiation and integration into simple algebraic multiplication and division. Used to model and analyze the behavior of electrical circuits and mechanical vibrations.

➤ **Use of Inverse Laplace Transforms (Question 2):** Translates the algebraic solution found in the **$p\text{-domain}$** back into a readable **$x\text{-domain}$** format. Determines how a physical system will actually react over time when given a specific input or "impulse."

---

## Procedure/Method used
The Laplace Transform is defined as: <br>
**$L[f(x)] = \int_0^{\infty} e^{-px} f(x) \, dx = F(p)$** 

Following are the procedures that describes the Laplace Transforms:

➤ **Procedure for Laplace Transforms:** <br>
The goal is to transform a function of time **_f(x)_** into a function of the complex frequency **_F(p)_**.

   1. **Linearity Check:** If the function is a sum, such as **_f(x) = g(x) + h(x)_**, split it into individual parts i.e. **_L{g(x)} + L{h(x)}_**.

   2. **Identify the Core Function:** Looking for the basic trigonometric (sin, cos), hyperbolic, or power (**_x<sup>n</sup>_**) function within the expression.

   3. **Apply the First Shifting Theorem:** If the function is multiplied by **$e^{ax}$**, first we find the Laplace of the core function and then replace every **_p_** with **_(p - a)_**. <br>
   **Formula:** **$L\{{e^{ax}f(x)\}} = F(p - a)$**

   4. **Using Simple Transform Pairs:** Using the Simple Transform Pairs Table to convert the core function.
   <img width="362" height="533" alt="image" src="https://github.com/user-attachments/assets/4fdc0286-f0f3-4b08-93c5-82642b175017" />
   
<br>

   5. **Simplification:** Combining the algebraic fractions into their simplest form.

<br>

➤ **Procedure for Inverse Laplace Transforms:** <br>
The goal is to take a frequency domain function **_F(p)_** and return it to the time domain **_f(x)_**

   1. **Denominator Analysis:** If the denominator is a quadratic that cannot be factored (like **$p^2 + 2p + 5$**), then use Completing the Square to get it into the form **$(p + a)^2 + b^2$**. Using Partial Fraction Decomposition to break complex fractions into simpler terms.

   2. **Numerator Matching:** Adjusting the numerator to match the standard forms of Sine or Cosine. If **$(p + a)^2$** in the denominator, the numerator must also be expressed in terms of _(p + a)_ to allow for an Inverse Shift.

   3. **Apply the Inverse Shifting Theorem:** Identify the shift **$(p + a)^2$**. This tells the final time-domain function must be multiplied by **$e^{ax}$**. <br>
   **Formula:** **$L^{-1}\{F(p - a)\} = e^{ax}f(x)$**

   4. **Inverse Mapping:** Using the Standard Transform Pairs Table in reverse to find the original function.

---


## Algorithm/Coding Approach: <br>
The following are the Algorithm/Coding Approach:

  ➤ **Symbolic Processing:** Using SymPy to treat variables as algebraic symbols for exact calculus instead of numerical approximations.

  ➤ **Automated Transforms:** Employs built-in functions like laplace_transform with pre-defined assumptions (*real*, *positive*) to ensure clean, convergent results.

  ➤ **Lambdification:** Using sp.lambdify to convert symbolic formulas into NumPy functions, making them compatible with numerical plotting.

  ➤ **Result Cleaning:** Automatically removes the Heaviside step function via .replace() to improve output readability and prevent graphing errors.

  ➤ **Modular Architecture:** Organizes the logic into separate functions for math problems, plotting, and the main menu for better maintainability.

  ➤ **Interactive Interface:** Implements a while loop and user input to provide a continuous, menu-driven command-line experience.

---


## Output Results
<img width="1243" height="550" alt="Output Result-1 - Copy" src="https://github.com/user-attachments/assets/d814f82c-e2c6-4be3-b8bb-af73ed3b98fe" />
<img width="1243" height="529" alt="Output Result-3 - Copy" src="https://github.com/user-attachments/assets/9daff858-2dc9-4362-b32b-2c3adea1a4d6" />
<img width="1242" height="359" alt="Output Result-4 - Copy" src="https://github.com/user-attachments/assets/505f821a-f5ae-4d29-9563-0a5fc590af62" />

---


## Solution Graphs from the Code <br>

## Solution Graphs based on problems To solve the following Laplace Transform problems (Question 1): <br>

### 1.) a.) Solution Graph of the problem **$x^5 \ e^{-2x}$**
<img width="1366" height="714" alt="image" src="https://github.com/user-attachments/assets/2cf85cd1-5090-4dbf-8ff3-4ee8457a8dba" />
<br><br>

### 1.) b.) Solution Graph of the problem **$(1 - x^2) \ e^{x}$**
<img width="1366" height="714" alt="image" src="https://github.com/user-attachments/assets/0d35e018-947a-40bf-950b-db7ecacc8774" />
<br><br>

### 1.) c.) Solution Graph of the problem **$e^{3x} \cos 2x$** 
<img width="1366" height="714" alt="image" src="https://github.com/user-attachments/assets/5d77af9d-5fd3-40af-8c30-ea48abfbbd0f" />
<br><br><br>


## Solution Graphs based on problems To solve the following Inverse Laplace Transform problems (Question 2): <br>

### 2.) a.) Solution Graph of the problem $\frac{6}{(p+2)^2 + 9}$ 
<img width="1366" height="720" alt="image" src="https://github.com/user-attachments/assets/456ae0bb-d722-46ce-9b8c-b5b31c1797d7" />
<br><br>

### 2.) b.) Solution Graph of the problem $\frac{12}{(p+3)^4}$
<img width="1366" height="712" alt="image" src="https://github.com/user-attachments/assets/850f5896-d03b-4e04-94be-4919b0c24d3d" />
<br><br>

### 2.) c.) Solution Graph of the problem $\frac{p+3}{p^2 + 2p + 5}$
<img width="1366" height="716" alt="image" src="https://github.com/user-attachments/assets/7956b468-dc93-452d-83ca-693fa7f216e0" />
<br><br>
