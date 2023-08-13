import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Training data
x_train = np.random.rand(100).astype(np.float32)
y_train = 2 * x_train + 1 + np.random.normal(0, 0.1, size=100).astype(np.float32)

# Create the model
model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(units=1, input_dim=1))

# Compile the model
model.compile(optimizer='sgd', loss='mean_squared_error')

# Train the model
model.fit(x_train, y_train, epochs=100, verbose=1)

# Display model parameters
weights = model.layers[0].get_weights()[0]
bias = model.layers[0].get_weights()[1]
print("Weights: {}".format(weights))
print("Bias: {}".format(bias))

# Plot training data and regression line
plt.scatter(x_train, y_train, label='Training Data')
plt.plot(x_train, weights * x_train + bias, color='red', label='Regression Line')
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Linear Regression using TensorFlow')
plt.show()

# Prediction for new data
x_new = np.array([0.2, 0.5, 0.8], dtype=np.float32)
y_pred = model.predict(x_new)
print("Predictions for new data:")
for i in range(len(x_new)):
    print("x = {}, y_pred = {}".format(x_new[i], y_pred[i][0]))
