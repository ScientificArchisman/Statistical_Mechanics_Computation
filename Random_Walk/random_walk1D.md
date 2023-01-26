# Random walk in 1D
- There are only 2 possibilities for the next step: left or right
- The step size is always 1
- The next step is independent of the previous step
- Probability of going left is p and probability of going right is 1-p
---


## Examples
- A drunkard w alking on a straight road
- A molecule moving in a liquid
- A particle moving in a gas  

Up/down, left/right, forward/backward are all examples of 1D random walk.  

## Example of Drunk Person
---
1. Choose step length = $l$(let)
2. Let probability of going right = $p$. Then probability of going left $= 1-p = q$(say).  
Evidently, $p+q = 1$.
3. Let number of steps = $n$.  
n should be a large number.
4. Number of steps to the right = $n_1$
5. Number of steps to the left = $n_2$

## Questions to answer
---
1. **Probability of taking $n_1$ steps to the right out of $N$ steps** $\\$
$$ P(n_1) = C_{n_1}^N \;p^{n_1} \; q^{N - n_1}$$
2. **Probability of taking $n_2$ steps to the left out of $N$ steps** $\\$
$$ P(n_2) = C_{n_2}^N \;q^{n_2} \; p^{N - n_2}$$

**NOTE:** 
- Observe that $n_1 + n_2 = N$
- Observe that $P(n_1) = P(n_2)$

3. **What is the probability of ending up at $ x = ml $** ?$\\$ 
This is the same as asking the probability of taking $n_1$ steps to the right or $n_2$ steps to the left and ending up at $x = ml$.
$$ P(x = ml) = P(n_1) = P(n_2)$$

### This distribution is called **Binomial Distribution**.
**Why Binomial?**
- Since the structure of $P(n_1)$ and $P(n_2)$ is same as that of binomial distribution, we can say that the distribution is binomial.

# Example Questions
A person is standing at x = 0. He takes N = 1,00,000 steps of step length = 1cm. Probability of taking a step to the right is $p = \frac{1}{3}$ .

1. What is the probability of taking 1,200 steps to the right?
2. What is the probability of taking 15,000 steps to the left?
3. What is the probability of returning to the starting point after 1,00,000 steps?
4. What is the probability that he will be at x = 20,000 cm after 1,00,000 steps?

**Solution:**
1. $P(n_1) = C_{n_1}^N \;p^{n_1} \; q^{N - n_1}$

$$P(1,200) = C_{1,200}^{1,00,000} \; \left(\frac{1}{3}\right)^{1,200} \; \left(\frac{2}{3}\right)^{80,800}$$

$$P(1,200) = \frac{1,00,000!}{1,200! \; 80,800!} \; \left(\frac{1}{3}\right)^{1,200} \; \left(\frac{2}{3}\right)^{80,800}$$
$$\\\ \\\$$

2. $P(n_2) = C_{n_2}^N \;q^{n_2} \; p^{N - n_2}$
$$P(15,000) = C_{15,000}^{1,00,000} \; \left(\frac{2}{3}\right)^{15,000} \; \left(\frac{1}{3}\right)^{85,000}$$

$$P(15,000) = \frac{1,00,000!}{15,000! \; 85,000!} \; \left(\frac{2}{3}\right)^{15,000} \; \left(\frac{1}{3}\right)^{85,000}$$

$$\\\ \\\$$
3. $x = n_1l - n_2l$
$$x = 0 \\
n_1 = n_2 \\
m = n_1 - n_2 \\
\therefore m = 0 \\
n_1 + n_2 = N = 1,00,000 \\
\therefore n_1 = n_2 = 50,000\\ 
\\\
P(n_1) = P(n_2) = \frac{1,00,000!}{50,000! \; 50,000!} \; \left(\frac{1}{3}\right)^{50,000} \; \left(\frac{2}{3}\right)^{50,000}$$

$$\\\ \\\$$
4. $x = n_1l - n_2l$
$$ x = ml \\\
\\
m = \frac{x}{l} = \frac{20,000}{1} = 20,000 \\\
\\
m = 20,000  \\
\\
n_1 + n_2 = N = 1,00,000 \\
\\
n_1 - n_2 = m \\
\\
20,000 = n_1 - n_2 \\
100,000 = n_1 + n_2 \\
\\
n_1 = 60,000 \\
n_2 = 40,000 \\
\\
P(n_1) = P(n_2) = \frac{1,00,000!}{60,000! \; 40,000!} \; \left(\frac{1}{3}\right)^{60,000} \; \left(\frac{2}{3}\right)^{40,000}$$ 
