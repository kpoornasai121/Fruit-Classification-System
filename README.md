# Fruit Classification Project

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![License](https://img.shields.io/badge/License-MIT-green)

Hey there! Welcome to my Fruit Classification project—a fun exploration of machine learning to identify fruits based on their physical traits. I’m Poornasai, and I built this to predict fruit types like apples, mandarins, oranges, and lemons using features like mass, width, height, and color score. The project includes a Jupyter notebook for analysis and a cool Streamlit app to make predictions interactively. Let’s dive into the world of fruits! 🍎🍊

Check out my GitHub: [kpoornasai121](https://github.com/kpoornasai121)

## What’s This Project About?

This project uses the [Fruit Dataset](https://www.kaggle.com/datasets/mjamilmoughal/fruits-with-colors-dataset) to classify fruits into categories (apple, mandarin, orange, lemon) based on features like mass, width, height, and color score. It leverages Python for data analysis, visualization, and machine learning, with a Random Forest model to make predictions. The Streamlit app lets you input fruit characteristics and get instant predictions, making it both educational and interactive.

## Cool Features

- **Data Exploration**: Peek into fruit traits with stats and visualizations.
- **Feature Importance**: See which features (like mass or color score) matter most for predictions.
- **Machine Learning**: Uses a Random Forest model for accurate fruit classification.
- **Interactive App**: A Streamlit interface to predict fruit types with sliders for input.
- **Beginner-Friendly**: Clear code and setup for anyone learning ML or Python.

## What Data Powers It?

The dataset (`fruit_data_with_colors.txt`) contains 59 fruit samples with the following columns:
- **fruit_label**: Numeric label (1=apple, 2=mandarin, 3=orange, 4=lemon).
- **fruit_name**: Fruit type (target variable).
- **fruit_subtype**: Variety (e.g., granny_smith).
- **mass**: Weight in grams.
- **width**: Width in cm.
- **height**: Height in cm.
- **color_score**: Color intensity (0 to 1).

**Size**: 59 rows, 7 columns, no missing values.

## Getting Started

Ready to classify some fruits? Here’s how to set it up:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/kpoornasai121/Fruit-Classification-System.git
   cd fruit-classification
     ```

2. **Get the Dataset**:
- Download fruit_data_with_colors.txt from the project folder or [source](https://github.com/UC Irvine Machine Learning Repository/fruit_data_with_colors.txt).
- Place it in a data folder in the project directory.

3. **Run the Notebook**:
  ```bash
  jupyter notebook
  ```
Open fruits.ipynb to explore the analysis and model training.

4. **Launch the Streamlit App**:
  ```bash
  streamlit run app.py
  ```
Access it at http://localhost:8503 to predict fruit types interactively.


## How to Use It
1. **Explore the Notebook**:
- Run fruits.ipynb to see data loading, stats, and a feature importance plot.
- Check the Random Forest model setup (training code is implied).

2. **Run the Streamlit App**:
- Start the app with streamlit run app.py.
- Use sliders to input mass, width, height, and color score.
- Click “Predict Fruit Type” to see the predicted fruit (e.g., apple or orange).

## Stuff You’ll Need
- Python 3.8 or higher
- Jupyter Notebook
- Streamlit
- Libraries: pandas, numpy, matplotlib, seaborn, scikit-learn, xgboost, joblib

**Install all of them with**:
  ```bash
  pip install jupyter pandas numpy matplotlib seaborn scikit-learn xgboost joblib streamlit
  ```

## License
This project is under the MIT License—free to use, modify, or share. See the  file for details.

