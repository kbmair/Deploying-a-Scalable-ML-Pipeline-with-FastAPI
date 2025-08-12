# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
The model here is a Random Forest Classifier that is trained to predict if an individual's income is greater than $50,000 per a year based on available census data. 
The model was trained using processed features from the census data.

## Intended Use
The model is intended to assist in income classification tasks based on demographic features. It could be used in applications like socio-economic research, targeted marketing, and many other instances.

## Training Data
As mentioned above, the model was trained on the publicly available census dataset which contains demographic data such as age, workclass, education, marital status, occupation, and hours worked per a week to name a few. 

## Evaluation Data
The evaluation was performed on the test data split from the original census dataset. This test step was preprocessed using the same pipeline as the training data to ensure consistency.

## Metrics
My model's performance was measured using precision, recall, and F1 score. On the test dataset, the model acheived: 
Precision: 0.7419
Recall: 0.6384
F1 Score: 0.6863

Also the model performance was analyzed on slices of the data that were grouped together by categorical features, with the same metrics recorded per feature value. This can be found in the slice_output.txt file.

## Ethical Considerations
This model uses demographic census information that may be sensitive, including race, sext, and marital status. There is a risk of bias in predictions if the training data reflects historical inequalities or sampling bias. Users should be cautious in this way when deploying the model.

## Caveats and Recommendations
It is always good to update the model with fresh data and carefully monitor the model for biases.