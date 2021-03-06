# Machine Learning && Deep Learning Basics

Syntesizing new knowledge by learning from data w/ the use of 'pattern recognition'.

### Supervised Learning
 - Most common form of ML
 - Training data submitted w/ desired output value
 - Good for "Clasification Problems" - system must attribute new data to known classes
 - "Feature Vector" - input vector
 - Training is performed by the minimization of a loss function 
 - cost function(), loss/error = desired output system - actual output
 - "Validation set" - Measures the acuracy of the model

### Unsupervised Learning
 - Unlabeled input data
 - System organizes data by common characteristics
 - Good for "Clustering Problems" where you don't know the outcome groups in advance

### Deep Learning
 - Good for NLP - (Natural Language Processing)
 - Each level corresponds to a different area of the cerebral cortex

### TensorFlow
 - "Tensor" =  multi-dimensional array
 - Defining, optimizing, and efficiently calculating mathematical expressions involving multi-dimensional arrays 
 - Programming support of deep neural networks and machine learning techniques
 - TensorFlow will figure out which parts of the computation should be moved to the GPU

### Python
 - Programming! Yay!

### The TensorFlow Graph
 - "Node" 
      * Instance of an operation
 - "Normal Edges"
      * Carry data from output of one node to input of the next
 - "Special Edges"
      * Depedency w/o data
      *  i.e. "Happens before"
 - "Operation" 
      * A computation
 - "Kernel"
      * Defines the implementation of an operation on X device
 - "Session"
      * Connection to tensorflow runtime

### Examples:

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

Assign a placeholder variable
```
a = tf.placeholder("int32")
```

Before you can use tensorflow objects in the graph (runtime) you need to initialize them first
```
model = tf.initialize_all_variables()
```

To run the tensorflow calulations
```
with tf.Session() as session:
    session.run(model)
```

Add default values to your session for your placeholders
```
sess.run(y, feed_dict={a: 2, b: 5})
```

To output the current graph to tensorboard
```
merged = tf.merge_all_summaries()
writer = tf.train.SummaryWriter("/tmp/tensorflowlogs",session.graph) 
```

To start tensorboard run
```
tensorboard --logdir=/tmp/tensorflowlogs
```

