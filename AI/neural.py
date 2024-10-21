import numpy as np

class NeuralNetwork():

    def __init__(self):
        np.random.seed(1)


        self.synaptic_weights = 2 * np.random.random((3,1)) - 1


    def sigmoid(self, x):
        return 1/(1 + np.exp(-x))
    
    def sidmoid_derivative(self,x):
        return x * (1-x)
    
    def train(self, training_inputs, training_outputs, traiing_iterations):

        for iterations in range(traiing_iterations):
             output = self.think(training_inputs)

             error = training_outputs - output

             adjustments = np.dot(training_inputs.T, error *  self.sidmoid_derivative(output))

             self.synaptic_weights += adjustments

    def think(self,inputs):
        inputs = inputs.astype(float)

        output = self.sidmoid(np.dot(inputs, self.synaptic_weights))

        return output