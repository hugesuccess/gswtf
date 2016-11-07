# Deep Learning

### Deep learning techniques
 - (GPUs) have greatly reduced the time needed for training networks, lowering them 10/20 times.
 - more numerous datasets on which to train a system
 - consists of a set of methods that allow a system to obtain a hierarchical representation of the data on multiple levels
     * Achieved by combining simple units (not linear), each of which transforms the representation at its own level, starting from the input level, to a representation at a higher (slightly more abstract) level. With enough of these transformations, complex input-output functions can be learned.
 - multi-level architecture w/:
    * simple units, 
    * all subject to training, 
    * many of which carry non-linear transformations
 - Examples of Deep learning models:
    1. pixel --> edge --> texture --> motif --> part --> object
    2. character --> word --> word group --> clause --> sentence --> story
 - "Invariance" - Its propensity to ignore the irrelevant negligible aspects. Each unit transforms its input to improve its properties to select and amplify only the relevant aspects for classification purposes
 - With multiple levels of non-linear transformations, therefore, with a depth approximately between 5 and 20 levels, a deep learning system can:
    * Learn and implement extremely intricate and complex functions, 
    * Simultaneously very sensitive to the smallest relevant details, and 
    * Is extremely insensitive and indifferent to large variations of irrelevant aspects of the input data which can be, in the case of object recognition: image's background, brightness, or the position of the represented object.

### Convolutional Neural Networks
- Mainly for classification problems
- CNNs are designed to process data represented in the form of multiple arrays (color images), represented by three two-dimensional arrays containing a pixel's color intensity
- CNNs and operate directly on the images while ordinary NN's work on features extracted from images.
- Dominant approach for almost all the problems of recognition

#### CNN Architecture
- "Local receptive fields" - CNNs utilize spatial correlations that may exist within the input data. Each neuron of the first subsequent layer connects only some of the input neurons.
- "Convolution" - For Example: Each feature map needs 25 weights (5x5) and a bias (shared); that is 26 parameters in total. Assuming we have 20 feature maps, we will have 520 parameters to be defined. With a fully connected network, with 784 input neurons and, for example, 30 hidden layer neurons, we need 30 more 784x30 bias weights, reaching a total of 23.550 parameters.
- "Pooling" - Layers immediately positioned after the convolutional layers; these simplify the output information of the previous layer to it (the convolution)
    *  It takes the input feature maps coming out of the convolutional layer and prepares a condensed feature map
- Hidden neurons only process the input data it recieves ( receptive field )
- The deeper the level the higher the level of abstraction
- "Convolution" - slide a weight (bias, kernel, etx.) over a group of pixels -- extracting a smaller dataset
- "Shared weights" - The map of connections from the input layer to the hidden feature map.
- "Shared bias" - the same kernel used on different levels
    * The sharing of weights and bias reduces the parameters involved in a convolutional network
- Example:
    * For each feature map we need 25 weights (5x5) and a bias (shared); 26 total parameters. 
    * Assuming we have 20 feature maps, we will have 520 parameters to be defined. 
    * With a fully connected network, with 784 input neurons and 30 hidden layer neurons, we need 30 more 784x30 bias weights, reaching a total of 23.550 parameters


Let's summarize: there are the 28x28 input neurons followed by a convolutional layer with a local receptive field 5x5 and 3 feature maps. We obtain as a result of a hidden layer of neurons 3x24x24. Then there is the max-pooling applied to 2x2 on the 3 regions of feature maps getting a hidden layer 3x12x12. The last layer is fully connected: it connects all the neurons of the max-pooling layer to all 10 output neurons, useful to recognize the corresponding output.

This network will then be trained by gradient descent and the back propagation algorithm

### CNN's w/ TensorFlow
