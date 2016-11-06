# Doing Math w/ TensorFlow

### Tensor Data Structure

 - Rank  - '# of dimensions
 - Shape - '# of Rows && Columns
 - Type  - datatype assigned to each tensor element 

#### Numpy
 - Used to build n-dimensional arrays

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

