# Starting w/ Machine Learning

### Linear Regression
 - y = Ax + b
 - A model to predict the values of a dependent variable from the values of one or more independent variables
    * TensorFlow must predict values of y as a function of x data according to our data model
 - The linear regression algorithm will determine the values of the constants A and b (fixed for our data model), which are then the true unknowns of the problem
 - 

### Mean Square Error
 - Cost function
 - returns a value that estimates how well the parameters are correct
 - a small value of this function corresponds to a best estimate for the unknown parameters A and b.
 - To minimize cost_function, we use an optimization algorithm with the "gradient descent"
 - gradient descent -> only a local function minimum
    *  If the number of minima of the function is limited, and there are very high number of attempts, then there is a good chance that sooner or later the global minimum will be identified

```
cost_function = tf.reduce_mean(tf.square(y - y_point))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(cost_function)
```

### MNIST -- Handwritten Digits

Handwritten numbers dataset available [here]( http://yann.lecun.com/exdb/mnist/)

### Classifiers
 - "Classification" identifies an algorithmic procedure that assigns each new input datum (instance) to one of the possible categories (classes)
 - In the supervised learning category
 - Basic steps:
    1. Build the training examples
    2. Choose the classifier / algorithm implementation
    3. Train the algorithm on the training set
    4. Evaluate the accuracy by applying a set of new instances (test set)

### K-Nearest Neighbor (KNN)
 - a supervised learning algorithm for both classification or regression
 - distance, d, is defined as the "Euclidean distance" (hypotonuese of a triangle) between two points
 - Can classify objects whose classes are not linearly separable
 - Pro's
    1. Stable classifier
        * Small data perturbations do not significantly affect the results
 - Con's
    1.  Not a true mathematical model
        * For every new classification, implemented by adding the new data to all initial instances and repeating the calculation procedure for the selected K value
    2. Requires a high amount of data to make realistic predictions
    3. Is sensitive to the noise of the analyzed data
