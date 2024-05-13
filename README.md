### Credit Approval Prediction

This project is a simple credit approval prediction application built using Streamlit. It uses a pre-trained machine learning model to predict the approval status of a loan based on user input.

#### Steps to Run the Application

1. **Install Streamlit**: If you haven't already, install Streamlit by running `pip install streamlit`.

2. **Clone the Repository**: Clone the repository containing the code for the application.

3. **Install Dependencies**: Navigate to the project directory and install the required dependencies by running `pip install -r requirements.txt`.

4. **Run the Application**: Use the command `streamlit run app.py` to start the Streamlit application.

5. **Interact with the Application**: Once the application is running, you can interact with it in your web browser. Fill in the required information in the input fields and click the "Predict Loan Approval" button to see the predicted loan status.

6. **View the Prediction**: The application will display the predicted loan status, which can be "Omitted," "Denied," or "Approved," based on the input provided.

7. **Repeat Prediction**: You can fill in different values in the input fields and click the button again to see how the predicted loan status changes based on the input.

### Note
Make sure to have the `model.pkl` file available in the same directory as `app.py`, as the application loads this pre-trained model to make predictions.
