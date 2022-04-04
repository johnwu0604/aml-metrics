import mlflow
import time 
import random

# Hypothetical scenario of iterating through an epoch
for x in range(100):
    # Printing epoch to generate logs
    print('Epoch: {}'.format(x))

    # Log an integer or float
    mlflow.log_metric('accuracy', float(x/100))

    # Log some text
    mlflow.log_text('epoch', 'epoch {}'.format(x))

    # Log a boolean
    mlflow.log_metric('random_boolean', bool(random.getrandbits(1)))

    # sleep for some time period
    time.sleep(15)