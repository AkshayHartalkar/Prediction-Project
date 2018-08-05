from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import tensorflow as tf
from DiabetesPrediction.swineflupred import flu_data as iris_data


parser = argparse.ArgumentParser()
parser.add_argument('--batch_size', default=100, type=int, help='batch size')
parser.add_argument('--train_steps', default=1000, type=int,help='number of training steps')

def main(Inputdata):
    (train_x, train_y), (test_x, test_y) = iris_data.load_data()

    # Feature columns describe how to use the input.
    my_feature_columns = []
    for key in train_x.keys():
        my_feature_columns.append(tf.feature_column.numeric_column(key=key))

    # Build 2 hidden layer DNN with 10, 10 units respectively.
    classifier = tf.estimator.DNNClassifier(
        feature_columns=my_feature_columns,
        hidden_units=[512,512],
        n_classes=4)

    # Train the Model.
    classifier.train(
        input_fn=lambda:iris_data.train_input_fn(train_x, train_y,100),steps=100)

    # Evaluate the model.34
    eval_result = classifier.evaluate(
        input_fn=lambda:iris_data.eval_input_fn(test_x, test_y,100))

    print('\nTest set accuracy: {accuracy:0.3f}\n'.format(**eval_result))

    # Generate predictions from the model
    expected = ["NotLikely",'LessLikely','MoreLikely','MostLikely']

# predict_x = {'BodyTempreture': [101.0],
    #              'RunnyNose': [0],
    #              'Headache': [1],
    #              'SoreThroat': [0],
    #              'Cough': [0],
    #              'PresenceOfBodyCold': [1],
    #              'Appetite': [2],
    #              'Tirednes': [1],
    #              'Diarrhoea': [0],
    #              'Vomiting': [1],
    #              'AchingMuscles': [0],
    # }
    predict_x = {'BodyTempreture': [Inputdata[0]],
                 'RunnyNose': [Inputdata[1]],
                 'Headache': [Inputdata[2]],
                 'SoreThroat': [Inputdata[3]],
                 'Cough': [Inputdata[4]],
                 'PresenceOfBodyCold': [Inputdata[5]],
                 'Appetite': [Inputdata[6]],
                 'Tirednes': [Inputdata[7]],
                 'Diarrhoea': [Inputdata[8]],
                 'Vomiting': [Inputdata[9]],
                 'AchingMuscles': [Inputdata[10]],
    }

    predictions = classifier.predict(
        input_fn=lambda:iris_data.eval_input_fn(predict_x,
                                                labels=None,
                                                batch_size=100))

    template = ('\nPrediction is "{}" ({:.1f}%), expected "{}"')

    for pred_dict, expec in zip(predictions, expected):
        class_id = pred_dict['class_ids'][0]
        probability = pred_dict['probabilities'][class_id]

        print(template.format(iris_data.SPECIES[class_id],100 * probability, expec))
        accuracy = 100 * probability

    return iris_data.SPECIES[class_id], accuracy

if __name__ == '__main__':
    tf.logging.set_verbosity(tf.logging.INFO)
    tf.app.run(main)
