What is Random Variable?
Random variable in statistics is a mathematical concept that assigns numerical values to outcomes of a sample space. There are two types of Random Variables, Discrete and Continuous. A random variable is considered a discrete random variable when it takes specific, or distinct values within an interval. Conversely, if it takes a continuous range of values, then it is classified as a continuous random variable. Random variables are generally represented by capital letters like X and Y. This is explained by the example,

Example: If two unbiased coins are tossed then find the random variable associated to that event.

Solution:

Suppose Two (unbiased) coins are tossed

X = number of heads. [X is a random variable or function]

Here, the sample space S = {HH, HT, TH, TT}

Random Variable Definition

We define random variable a function which maps from sample space of an experiment to the real numbers. Mathematically, Random Variable is expressed as,

X: S →R

where,

X is Random Variable (It is usually denoted using capital letter)
S is Sample Space
R is Set of Real Numbers
Suppose a random variable X takes m different values i.e. sample space

X = {x1, x2, x3………xm} with probabilities

P(X = xi) = pi

where 1 ≤ i ≤ m

The probabilities must satisfy the following conditions :

0 ≤ pi ≤ 1; where 1 ≤ i ≤ m
p1 + p2 + p3 + ……. + pm = 1 Or we can say 0 ≤ pi ≤ 1 and ∑pi = 1
Hence possible values for random variable X are 0, 1, 2.

X = {0, 1, 2} where m = 3

P(X = 0) = (Probability that number of heads is 0) = P(TT) = 1/2×1/2 = 1/4
P(X = 1) = (Probability that number of heads is 1) = P(HT | TH) = 1/2×1/2 + 1/2×1/2 = 1/2
P(X = 2) = (Probability that number of heads is 2) = P(HH) = 1/2×1/2 = 1/4
Here, you can observe that, (0 ≤ p1, p2, p3 ≤ 1/2)

p1 + p2 + p3 = 1/4 + 2/4 + 1/4 = 1

For example,

Suppose a dice is thrown (X = outcome of the dice). Here, the sample space S = {1, 2, 3, 4, 5, 6}. The output of the function will be:

P(X=1) = 1/6
P(X=2) = 1/6
P(X=3) = 1/6
P(X=4) = 1/6
P(X=5) = 1/6
P(X=6) = 1/6
Types of Random Variable
Random variable are of two types that are,

Discrete Random Variable
Continuous Random Variable
Random-Variable Classification

Discrete Random Variable
A random variable X is said to be discrete if it takes on a finite number of values. The probability function associated with it is said to be

PMF = Probability Mass Function P(xi), if

0 ≤ pi ≤ 1
∑pi = 1 where the sum is taken over all possible values of x
Discrete Random Variables Example

Example: Let S = {0, 1, 2}

xi

0

1

2

Pi(X = xi)

P1

0.3

0.5

Find the value of P (X = 0)

Solution:

We know that the sum of all probabilities is equal to 1. And P (X = 0) be P1

P1 + 0.3 + 0.5 = 1

P1 = 0.2

Then, P (X = 0) is 0.2

Continuous Random Variable
A random variable X is said to be continuous if it takes on an infinite number of values. The probability function associated with it is said to be PDF (Probability Density Function).

PDF (Probability Density Function)

If X is a continuous random variable. P (x < X < x + dx) = f(x)dx then,

0 ≤ f(x) ≤ 1; for all x
∫ f(x) dx = 1 over all values of x
Then P (X) is said to be PDF of the distribution.

Continuous Random Variables Example
Example: Find the value of P (1 < X < 2)

Such that,

f(x) = kx3; 0 ≤ x ≤ 3 = 0
Otherwise f(x) is a density function.

Solution:

If a function f is said to be a density function, then the sum of all probabilities is equal to 1.

Since it is a continuous random variable Integral value is 1 overall sample space s.

∫ f(x) dx = 1

∫ kx3 dx = 1

K[x4]/4 = 1

Given interval, 0 ≤ x ≤ 3 = 0

K[34 – 04]/4 = 1

K(81/4) = 1

K = 4/81

Thus,

P (1 < X < 2) = k×[X4]/4

P = 4/81×[16-1]/4

P = 15/81

Random Variable Formula
There are two main random variable formulas,

Mean of Random Variable
Variance of Random Variable
Let’s learn about the same in detail,

Mean of Random Variable

For any random variable X where P is its respective probability we define its mean as,

Mean(μ) = ∑ X.P

where,

X is the random variable that consist of all possible values.
P is the probability of respective variables



Variance of Random Variable

The variance of random variable tells us how the random variable is spread about the mean value of the random variable. Variance of Random Variable is calculated using the formula,

Var(x) = σ2 = E(X2) – {E(X)}2

where,

E(X2) = ∑X2P
E(X) = ∑XP
Random Variable Functions
For any random variable X if it assume the values x1, x2,…xn where the probability corresponding to each random variable is P(x1), P(x2),…P(xn), then the expected value of the variable is,

Expectation of X, E(x) = ∑ x.P(x)

Now for any new random variable Y in which the random variable X is its input, i.e. Y = f(X), then cumulative distribution function of Y is,

Fy(Y) = P(g(X) ≤ y)

Probability Distribution and Random Variable
For a random variable its probability distribution is calculated using three methods,

Theoretical listing of outcomes and probabilities of the outcomes.
Experimental listing of outcomes followed with their observed relative frequencies.
Subjective listing of outcomes followed with their subjective probabilities.
Probability of a random variable X that takes values x is defined using a probability function of X that is denoted by f (x) = f (X = x).

There are various probability distributions that are,

Binomial Distribution
Poisson Distribution
Bernoulli’s Distribution
Exponential Distribution
Normal Distribution
Also Check,

Probability Distribution Function
Expected Value
Variance and Standard Deviation
Random Variable Example
Example 1: Find the mean value for the continuous random variable, f(x) = x2, 1 ≤ x ≤ 3

Solution:

Given,

f(x) = x2

1 ≤ x ≤ 3

E(x) = ∫31 x.f(x)dx

E(x) = ∫31 x.x2.dx

E(x) = ∫31 x3.dx

E(x) = [x4/4]31

E(x) = 1/4{34– 14} = 1/4{81 – 1}

E(x) = 1/4{80} = 20

Example 2: Find the mean value for the continuous random variable, f(x) = ex, 1 ≤ x ≤ 3

Solution:

Given,

f(x) = ex

1 ≤ x ≤ 3

E(x) = ∫31 x.f(x)dx

E(x) = ∫31 x.ex.dx

E(x) = [x.ex – ex]31

E(x) = [ex(x – 1)]31

E(x) = e3(2) – e(0)

E(x) = 2e3

Practice Problems on Random Variable
P1. Find the mean value for the continuous random variable, f(x) = 3x3, 0 ≤ x ≤ 9

P2. Find the mean value for the continuous random variable, f(x) = x + sin x, 0 ≤ x ≤ π/4

P3. Find the variance value for the continuous random variable, f(x) = 2ex +x, -2 ≤ x ≤ 2

P4. Find the variance value for the continuous random variable, f(x) = 5 + x.tanx, -π/4 ≤ x ≤ π/4

FAQs on Random Variable
1. What is a Random Variable?

A random variable in statistics are the variables that represent all the possible outcome of a Random Variable.

2. What are Two Types of Random Variable?

There are two types of Random Variables and that are,

Continuous Random Variable
Discrete Random Variable
3. What is Mean of a Random Variable?

Mean of Random Variable is calculated using the formula,

Mean of a Discrete Random Variable: E[X] = ∑x.P(X = x)
Mean of a Continuous Random Variable: E[X] = ∫ x.f(x).dx
4. What is Variance of a Random Variable?

Variance of Random Variable is calculated using the formula,

Variance of a Discrete Random Variable: V[X] = ∑(x – μ)2.P(X = x)
Variance of a Continuous Random Variable: V[X] = ∫ (x – μ)2.f(x).dx
5. What is Random Variables Expected Value?

Expected value of a Random Variable is the weighted average of all possible values of the variable. Weight of the random variable is the probability of random variable at specific values.

6. What are Continuous Random Variables?

Continuous Random Variables are type of random variable in probability theory and statistics that are used to represent the continuous probability of the distribution of a function.

