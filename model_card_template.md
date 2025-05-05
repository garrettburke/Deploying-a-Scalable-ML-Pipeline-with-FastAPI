# Model Card

## Model Details
This model was created by Garrett Burke. The model uses the RandomForestClassifier() from sklearn.ensemble, with the default settings (no hyperparameters set).

## Intended Use
The intended use of the model is to predict whether an individual's income is above or below $50,000, based on the following inputs: age, workclass, fnlgt, education, education-num, marital-status, occupation, relationship, race, sex, capital-gain, capital-loss, hours-per-week, native-country. More information about the inputs is available here: https://web.archive.org/web/20230411111856/https://archive.ics.uci.edu/ml/datasets/census+income. The data was originally acquired from the 1994 U.S. Census database by Barry Becker. 

## Training Data
The training data was encoded using the OneHotEncoder method from sklearn with sparse_output set to False, and handle_unknown set to "ignore". The target "salary" was transformed to binary using LabelBinarizer().

## Evaluation Data
The evaluation data goes through the same process as the training data, although it uses the OneHotEncoder() and LabelBinarizer() object that is persisted following the training run.

## Metrics
Precision: 0.7420 | Recall: 0.6334 | F1: 0.6834

## Ethical Considerations
This data includes demographics information and should not be used for any purpose that could be interpreted as discriminatory. 

## Caveats and Recommendations
This dataset is from 1994, a little over 30 years ago. Much has changed in the world since then, and the results of this model should not be compared to present day.