import numpy as np

class NeuralNetwork():
    def __init__(self):
        np.random.seed(1)

        self.synaptic_weights = 2 * np.random.random((3,1)) - 1


    def sigmoid(self,x):
        return 1/(1 + np.exp(-x))

    def sigmoid_derivative(self,x):
        return x * (1 - x)

    def train(self, training_inputs, training_outputs, training_iterations):

        for iteration in range(training_iterations):

            output = self.think(training_inputs)

            error = training_outputs - output

            adjustments = np.dot(training_inputs.T, error *self.sigmoid_derivative(output))

            self.synaptic_weights += adjustments

    def think(self,inputs):

        inputs = inputs.astype(float)
        output = self.sigmoid(np.dot(inputs, self.synaptic_weights))

        return output


if __name__ == "__main__":

    ann = NeuralNetwork()

    print("Begning randomy generated weights")
    print(ann.synaptic_weights)

    training_inputs = np.array([[0,0,1],[1,1,1],[1,0,1],[0,1,1]])
    training_outputs = np.array([[0,1,1,0]]).T

    ann.train(training_inputs,training_outputs,1500)

    print("Endig weights after training")
    print(ann.synaptic_weights)

    ui1 = str(input("New input 1 : "))
    ui2 = str(input("New input 2 : "))
    ui3 = str(input("New input 3 : "))

    print("New Situation ", ui1,ui2,ui3)
    print("New output :" , ann.think(np.array([ui1,ui2,ui3])))