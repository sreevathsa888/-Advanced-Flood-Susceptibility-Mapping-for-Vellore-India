
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import joblib
import os

# --- Configuration ---
DATA_PATH = os.path.join('data', 'processed', 'final_training_data.csv')
MODEL_OUTPUT_PATH = os.path.join('data', 'outputs', 'model', 'flood_susceptibility_model.pkl')

# --- Main Script ---
def main():
    """Main function to load data, train model, and save it."""
    
    print("--- Starting Flood Susceptibility Model Training ---")

    # 1. Load Data
    try:
        data = pd.read_csv(DATA_PATH)
        print(f"Data loaded successfully from {DATA_PATH}. Shape: {data.shape}")
    except FileNotFoundError:
        print(f"Error: Training data not found at {DATA_PATH}")
        print("Please ensure you have generated the training data using QGIS and placed it correctly.")
        return

    # 2. Prepare Data
    # Drop columns not needed for training, like feature IDs or coordinates
    features = data.drop(columns=['fid', 'Class', 'point_id'], errors='ignore') 
    target = data['Class']
    print("Features selected for training:", list(features.columns))

    # 3. Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.3, random_state=42, stratify=target)
    print(f"Data split into {len(X_train)} training samples and {len(X_test)} testing samples.")

    # 4. Initialize and Train the Random Forest Model
    print("\nTraining Random Forest model...")
    # n_estimators=100 means 100 decision trees.
    # class_weight='balanced' helps when one class has more samples than the other.
    model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced', n_jobs=-1)
    model.fit(X_train, y_train)
    print("Model training complete.")

    # 5. Evaluate the Model
    print("\n--- Model Evaluation ---")
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy on Test Set: {accuracy * 100:.2f}%")

    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    
    # 6. Save the trained model
    os.makedirs(os.path.dirname(MODEL_OUTPUT_PATH), exist_ok=True)
    joblib.dump(model, MODEL_OUTPUT_PATH)
    print(f"\nModel successfully saved to: {MODEL_OUTPUT_PATH}")
    print("\n--- Process Finished ---")

if __name__ == '__main__':
    main()
