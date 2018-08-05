import pandas as pd
import tensorflow as tf
import csv
import random
import os

CSV_COLUMN_NAMES = ['Pregnancies', 'Glucose','BloodPressure', 'SkinThickness', 'Insulin','BMI','diabetesPedigreeFunction','age','outcome']
SPECIES = ["yes", "no"]
#
# def splitDataset(dataset, splitRatio):
#     trainSize = int(len(dataset) * splitRatio)
#     trainSet = []
#     copy = list(dataset)
#     while len(trainSet) < trainSize:
#         index = random.randrange(len(copy))
#         trainSet.append(copy.pop(index))
#     return [trainSet, copy]
#
# def loadCsv(filename):
#     lines = csv.reader(open(filename, "r"))
#     dataset = list(lines)
#     for i in range(len(dataset)):
#         dataset[i] = [float(x) for x in dataset[i]]
#     return dataset

def maybe_download():
    # filename = 'pima-indians-diabetes.data.csv'
    # splitRatio = 0.67
    # dataset = loadCsv(filename)
    # train_path, test_path = splitDataset(dataset, splitRatio)
    # with open('test.csv','w') as f:
    #     for line in test_path:
    #         f.write('\n')
    #         for l in line:
    #             f.write(str(l)+",")
    test_path = os.path.abspath("test.csv")
    train_path = os.path.abspath("train.csv")
    return train_path, test_path

def load_data(y_name='outcome'):
    """Returns the iris dataset as (train_x, train_y), (test_x, test_y)."""
    train_path, test_path = maybe_download()

    train = pd.read_csv(train_path, names=CSV_COLUMN_NAMES,header=0)
    train_x, train_y = train, train.pop(y_name)

    test = pd.read_csv(test_path, names=CSV_COLUMN_NAMES,header=0)
    test_x, test_y = test, test.pop(y_name)

    return (train_x, train_y), (test_x, test_y)


def train_input_fn(features, labels, batch_size):
    """An input function for training"""
    # Convert the inputs to a Dataset.
    dataset = tf.data.Dataset.from_tensor_slices((dict(features), labels))

    # Shuffle, repeat, and batch the examples.
    dataset = dataset.shuffle(1000).repeat().batch(batch_size)

    # Return the dataset.
    return dataset


def eval_input_fn(features, labels, batch_size):
    """An input function for evaluation or prediction"""
    features=dict(features)
    if labels is None:
        # No labels, use only features.
        inputs = features
    else:
        inputs = (features, labels)

    # Convert the inputs to a Dataset.
    dataset = tf.data.Dataset.from_tensor_slices(inputs)

    # Batch the examples
    assert batch_size is not None, "batch_size must not be None"
    dataset = dataset.batch(batch_size)

    # Return the dataset.
    return dataset


# The remainder of this file contains a simple example of a csv parser,
#     implemented using a the `Dataset` class.

# `tf.parse_csv` sets the types of the outputs to match the examples given in
#     the `record_defaults` argument.
CSV_TYPES = [[0],[0],[0],[0],[0],[0.0],[0.0],[0],[0]]

def _parse_line(line):
    # Decode the line into its fields
    fields = tf.decode_csv(line, record_defaults=CSV_TYPES)

    # Pack the result into a dictionary
    features = dict(zip(CSV_COLUMN_NAMES, fields))

    # Separate the label from the features
    label = features.pop('outcome')

    return features, label


def csv_input_fn(csv_path, batch_size):
    # Create a dataset containing the text lines.
    dataset = tf.data.TextLineDataset(csv_path)

    # Parse each line.
    dataset = dataset.map(_parse_line)

    # Shuffle, repeat, and batch the examples.
    dataset = dataset.shuffle(1000).repeat().batch(batch_size)

    # Return the dataset.
    return dataset
