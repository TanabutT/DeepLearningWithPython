# DeepLearningWithPython

Start DeepLearning Journey to prepare for Thesis

Keras basic













note:

print("{:45} | {}".format('Raw Model Predictions','True labels'))
for i,pred in enumerate(preds):
  print("{} | {}".format(pred,competitors_small_test[i]))
  
output:
Raw Model Predictions                         | True labels
[0.34438723 0.00842557 0.63167274 0.01551455] | [0. 0. 1. 0.]
[0.0989717  0.00530467 0.07537904 0.8203446 ] | [0. 0. 0. 1.]
[0.33512568 0.00785374 0.28132284 0.37569773] | [0. 0. 0. 1.]
[0.8547263  0.01328656 0.11279515 0.01919206] | [1. 0. 0. 0.]
[0.3540977  0.00867271 0.6223853  0.01484426] | [0. 0. 1. 0.]


# Extract the position of highest probability from each pred vector
preds_chosen = [np.argmax(pred) for pred in preds]

# Print preds vs true values
print("{:10} | {}".format('Rounded Model Predictions','True labels'))
for i,pred in enumerate(preds_chosen):
  print("{:25} | {}".format(pred,competitors_small_test[i]))
    
  np.argmax will return index of max value
