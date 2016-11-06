### Machine Learning && Deep Learning Basics

Syntesizing new knowledge by learning from data w/ the use of 'pattern recognition'.

# Supervised Learning
 - Most common form of ML
 - Training data submitted w/ desired output value
 - Good for "Clasification Problems" - system must attribute new data to known classes
 - "Feature Vector" - input vector
 - Training is performed by the minimization of a loss function 
 - cost function(), loss/error = desired output system - actual output
 - "Validation set" - Measures the acuracy of the model

# Unsupervised Learning
 - Unlabeled input data
 - System organizes data by common characteristics
 - Good for "Clustering Problems" where you don't know the outcome groups in advance

# Deep Learning
 - Good for NLP - (Natural Language Processing)
 - Each level corresponds to a different area of the cerebral cortex

## TensorFlow
 - "Tensor" =  multi-dimensional arrays  
 

## Python
 - Programming! Yay!

Example Code:

Import the tensorflow package
```
import tensorflow as tf
```

Assign a constant value
```
x = tf.constant(1, name='x')
```

Assign a variable
```
y = tf.Variable(x + 9, name='y')
```

Before you can use tensorflow objects in the graph (runtime) you need to initialize them first
```
model = tf.initialize_all_variables()
```

To run the tensorflow calulations
```
with tf.Session() as session:
    session.run(model)
