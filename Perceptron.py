import matplotlib.pyplot as plt

class Perceptron():
    def __init__(self, num_features):
        self.num_features = num_features
        self.weights = []
        for i in range(num_features):
            self.weights.append([0.])
        self.bias = [0.]

    def forward(self, x):
        linear = []
        dot_product = 0;
        for i in range(len(x[0])):####problem
            dot_product += x[0][i] * self.weights[i][0]
        temp = []
        temp.append(dot_product)
        
        for i in range(len(temp)):
            temp[i] = temp[i]+ self.bias[0]
        linear.append(temp)
        
        ##get predictions
        prediction = []
        for i in range(len(linear)):
            if linear[0][i] > 0.:
                prediction.append([1])
            else:
                prediction.append([0])
        return prediction
        
    def backward(self, x, y):
        predictions = self.forward(x)
        errors = []
        for i in range(len(predictions)):
            errors.append(y - predictions[0][i])
        return errors
        
    def train(self, x, y, epochs):
        for e in range(epochs):
            for i in range(len(y)):
                temp = []
                temp.append(x[i])
                errors = self.backward(temp, y[i])
                extra_term = []
                for a in range(len(x[i])):
                    extra_term.append(errors[0] * x[i][a])
                for b in range(len(self.weights)):
                    self.weights[b][0] += extra_term[b]
                self.bias[0] += errors[0]
        
    def evaluate(self, x, y):
        sum = 0
        for i in range(len(x)):
            temp = []
            temp.append(x[i])
            predictions = self.forward(temp)
            if(predictions[0][0] == y[i]):
                sum = 1 + sum
        accuracy = sum / len(y)
        return accuracy
