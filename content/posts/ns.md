+++
title = 'softmax numerical instability'
date = 2024-10-10T05:05:54+05:30
draft = false
+++

# numerical instability of softmax

the softmax function is widely used in machine learning, especially for converting raw scores (logits) into probabilities in classification problems. it is defined as:


```
Softmax(z_i) = exp(z_i) / sum(exp(z_j) for j in range(n))

```

where `z_i` represents the logits for class `i`.

## the problem of numerical instability

the softmax function can suffer from **numerical instability**, particularly when the input logits `z` contain large or small values. this is because computing `exp(z_i)` can result in very large or very small numbers, leading to overflow or underflow errors when summed across all classes.

### overflow example

consider logits with large positive values, like `z = [1000, 1001, 1002]`. calculating the exponential values directly:


```
exp(1000) ≈ 2.688 × 10^434 exp(1001) ≈ 7.307 × 10^434 exp(1002) ≈ 1.987 × 10^435


```

the sum of these terms becomes extremely large, and may exceed the range of numbers that can be represented by floating-point arithmetic, resulting in **overflow**.

### underflow example

conversely, when logits contain large negative values, like `z = [-1000, -1001, -1002]`, their exponentials will be extremely small, close to zero, leading to **underflow**:


```
exp(-1000) ≈ 0 exp(-1001) ≈ 0 exp(-1002) ≈ 0
```


in this case, the sum of the exponentials can become numerically zero, causing issues when dividing to compute probabilities.

## mitigating numerical instability

a common trick to avoid numerical instability is to **subtract the maximum logit** from each input logit before applying the softmax function:



```
Softmax(z_i) = exp(z_i - max(z)) / sum(exp(z_j - max(z)) for j in range(n))


```


here, `max(z)` is the maximum value among the logits. subtracting it ensures that the largest exponent is zero, thus avoiding overflow. this transformation does not change the output of the softmax, as the scaling factor cancels out:

by doing this, we keep the exponentials in a more manageable range, improving numerical stability.
