# Doing Math w/ TensorFlow

### Tensor Data Structure

 - Rank  - '# of dimensions
 - Shape - '# of Rows && Columns
 - Type  - datatype assigned to each tensor element 

#### Numpy
 - Used to build n-dimensional arrays

### Partial Differential Equation
 - differential equation involving partial derivatives (results/outputs) of an unknown function of several independent variables
 - commonly used to solve physical problems in various fields, from quantum mechanics to financial markets.

### Examples

Create a 1d tensor w/ numpy
```
tensor_1d = np.array([1.3, 1, 4.0, 23.99])
```
Find the rank(# of dimensions) of a tensor
```
# Integer Value
tensor_1d.ndim 

# Tuple
tensor_1d.shape 
```

Find the tensor datatype
```
tensor_1d.dtype 
```
Create a 2d tensor
```
tensor_2d=np.array([(1,2,3,4),(4,5,6,7),(8,9,10,11),(12,13,14,15)]) 
```
Access the value of a 2d tensor
```
tensor_2d[3][3] 
```
Create a 3d tensor
```
tensor_3d = np.array([[[1,2],[3,4]],[[5,6],[7,8]]]) 
```

To retrieve an element from a three-dimensional tensor,
```
tensor_3d[plane,row,col]
```

Matrix Multiplication
```
matrix_product = tf.matmul(matrix1, matrix2) 
```

To compute a gradient
```
tf.gradients(x, y)
```

Random Numbers
```
# Uniform Distribution
random_uniform(shape, minval, maxval, dtype, seed, name) 

# Random Normal
tf.random_normal([100], mean=0, stddev=2) 
```

----------------------

### TensorFlow Operations

TensorFlow Operator | Description
:---: | --- | ---
tf.add | Returns the sum
tf.sub | Returns subtraction
tf.mul | Returns the multiplication
tf.div | Returns the division
tf.mod | Returns the module
tf.abs | Returns the absolute value
tf.neg | Returns the negative value
tf.sign | Returns the sign
tf.inv | Returns the inverse
tf.square | Returns the square
tf.round | Returns the nearest integer
tf.sqrt | Returns the square root
tf.pow | Returns the power
tf.exp | Returns the exponential
tf.log | Returns the logarithm
tf.maximum | Returns the maximum
tf.minimum | Returns the minimum
tf.cos | Returns the cosine
tf.sin | Returns the sine
