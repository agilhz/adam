import streamlit as st
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
import pandas as pd
import shap

# Load the necessary objects from the pickle file
with open('output_data.pickle', 'rb') as file:
    output_data = pickle.load(file)

cm = output_data['confusion_matrix']
feat_importances = output_data['feature_importances']
explainer = output_data['explainer']
shap_values = output_data['shap_values']

# Display the confusion matrix using Streamlit
st.subheader('Confusion Matrix')
fig, ax = plt.subplots(figsize=(12, 10))  # Set the desired size
sns.heatmap(cm, annot=True, fmt='d', cmap='YlOrBr', ax=ax)
st.pyplot(fig)

# Display the feature importance using Streamlit
st.subheader('Feature Importance')
fig, ax = plt.subplots(figsize=(12, 10))  # Set the desired size
feat_importances.nlargest(25).plot(kind='barh', color='chocolate', ax=ax)
ax.invert_yaxis()
st.pyplot(fig)

# Display the SHAP waterfall plot for Not Churn Customer using Streamlit
st.subheader('SHAP Values - Not Churn Customer')
fig, ax = plt.subplots(figsize=(12, 10))  # Set the desired size
shap.plots.waterfall(shap_values[0], show=False)
st.pyplot(fig)

# Display the SHAP waterfall plot for Churn Customer using Streamlit
st.subheader('SHAP Values - Churn Customer')
fig, ax = plt.subplots(figsize=(12, 10))  # Set the desired size
shap.plots.waterfall(shap_values[1], show=False)
st.pyplot(fig)
