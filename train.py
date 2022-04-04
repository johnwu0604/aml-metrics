import mlflow
import time 
import random

# Hypothetical scenario of iterating through an epoch
for x in range(100):
    # Printing epoch to generate logs
    print('Epoch: {}'.format(x))

    # Log some metrics
    mlflow.log_metric('accuracy', float(x/100 - random.uniform(0.005, 0.001)))
    mlflow.log_metric('loss', float(random.uniform(100, 200) - x))
    mlflow.log_metric('random_int', random.randrange(10))

    # sleep for some time period
    time.sleep(15)