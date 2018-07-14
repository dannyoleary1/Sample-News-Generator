from keras.callbacks import LambdaCallback
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.layers import LSTM
from keras.optimizers import RMSprop
from keras.utils.data_utils import get_file
import numpy as np
import random
import sys
import io

path = get_file('nietzsche.txt', origin="https://s3.amazonaws.com/text-datasets/nietzsche.txt")
with io.open(path, encoding='utf-8') as f:
    text = f.read().lower()

print ("Corpus Length: %s" % (len(text)))
print ("Type of text: %s" %(type(text)))