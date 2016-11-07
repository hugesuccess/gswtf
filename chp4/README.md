# Introducing Neural Networks

### What are Artificial Neural Networks
 - An artificial neural network (ANN) is an information processing system whose operating mechanism is inspired by biological neural circuits
    * Each unit or node simulates the role of the neuron in biological neural networks (the biological synapses)
    * Weighing the intensity of the transmitted signals, by multiplying them by the weights whose values depend on the connection itself
    * Each node ( artificial neuron ) becomes active if the total quantity of signal that it receives exceeds its activation threshold 
    * If a node becomes active, it emits a signal to the next connected node. Each connection point acts as a filter that converts the message into an inhibitory or excitatory signal, increasing or decreasing the intensity according to their individual characteristics.
    * Each neuron is connected with all those of the next layer
    * There are no connections between neurons belonging to the same layer
    * The number of layers and of neurons per layer depends on the problem to be solved
 - Architecture
    * Connection Path
    * # of layers ( the levels of nodes between input and outputs )
    * Number of neurons per layer

### Single Layer Perceptron
 - Local neuron memory is a vector (array) of weights, W = (w1, w2,......, wn)
 - Sum of the input vector X =(x1, x2,......, xn) is multiplied by the corresponding element of the vector of the weights; then the value provided in the output (weighted sum) will be the input of an activation function (???)
 - Returns 1 if the result is greater than a certain threshold, otherwise it returns -1.
 - Iterative learning procedure 
    * "Epoch" - learning cycle
 - Each epoch it slightly modifies the synaptic weights to minimize it's cost function.
 - After training must be tested w/ new data (validation set)

### Logistic Regression
 - Allows us to solve problems of supervised classification
 - Uses Logistic function ( AKA Sigmoid )
 - Dependent variable values strictly between 0 and 1
 - Function will tell the probability of beloging to class (1)
 - "Loss function" - indicates the degree to which the behavior of the network deviates from the desired one
 - Supervised learning - neural network is configured as an iterative process of optimization of the weights
    * Modified on the basis of the network's performance of the training set 
    * Aim is to minimize the loss function
 - The performance of the network is then verified on a test set, consisting of images other than those of trained
 - Steps
    1. The weights are initialized with random values at the beginning of the training.
    2. For each element of the training set the error is calculated and used to adjust the weights
    3. Repeat until error threshold reached or maximum iterations reached

### Building a Logistic Regression Model

Define x as the input tensor; it represents the MNIST data image of size 28 x 28 = 784 pixels
```
x = tf.placeholder("float", [None, 784]) 
```

Output tensor with 10 probabilities, each one corresponding to a digit (of course the sum of probabilities must be one)
```
y = tf.placeholder("float", [None, 10]) 

To evaluate the evidence, we first define the weights input tensor as W:
```
W = tf.Variable(tf.zeros([784, 10]))
```
The softmax function is specified in two main steps:
    1. Calculate the evidence that a certain image belongs to a particular class
    2. Convert the evidence into probabilities of belonging to each of the 10 possible classes


#### Softmax Step 1 - Evaluation
For a given image, evaluate the evidence for each class i by simply multiplying the tensor W with the input tensor x using TensorFlow. The model includes an extra parameter ( b ) representing the degree of uncertainty ( bias ).
```
evidence = tf.matmul(x, W) + b
```

#### Softmax Step 2 - Activation
Use the softmax function to obtain the output vector of probabilities. tf.nn.softmax provides a probability-based output from the input evidence tensor. Once we implement the model, we can find the weights W and biases b through the iterative training algorithm. In each iteration, the training algorithm takes the training data, applies the neural network, and compares the result with the expected.
```
activation = tf.nn.softmax(tf.matmul(x, W) + b)
```
In order to train our model and know when we have a good one, we must define how to define the accuracy of our model. Our goal is to try to get values of parameters W and b that minimize the loss value.

"Squared Euclidean Distance" -  A common measure of error is the mean squared error AKA "Hypotenuse formula"

We use the "cross-entropy" measure of error
```
cross_entropy = y * tf.lg(activation)
```

In order to minimize cross_entropy, we can use the following combination of tf.reduce_mean and tf.reduce_sum to build the cost function:
```
cost = tf.reduce_mean(-tf.reduce_sum(cross_entropy, reduction_indices=1)) 
```

Then we must minimize it using the gradient descent optimization algorithm:

```
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)
```

Few lines of code to build a neural net model!
