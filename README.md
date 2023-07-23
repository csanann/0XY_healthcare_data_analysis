
# The 0XY_Healthcare Data Analysis Project

This project is a learning exercise aimed at analyzing healthcare data with a focus on patient demographics, disease types, treatment types, and treatment outcomes. The goal is to gain a better understanding of the factors that contribute to successful treatment outcomes and to identify areas where healthcare provision could potentially be improved.

## Disclaimer

This project is for learning purposes only. The data used is publicly available and does not contain any sensitive or personal health information.

## Dataset

The data for this project is sourced from the [Patient Treatment Classification | Kaggle](https://www.kaggle.com/datasets/saurabhshahane/patient-treatment-classification).

## Tech/Tools

- Data Analysis: Python (pandas, NumPy, matplotlib, seaborn, scikit-learn)
- Data Storage: MongoDB/Mongoose
- Deployment: AWS S3
- Version Control: Git, Github
- Backend: Python and Flask
- Front-end Interface: React and Vite
- TDD, BDD: pytest for unit tests, integration tests, and functional tests. BDD: BDD framework like `behave` or `pytest-bdd`. Code coverage is measured with `pytest-cov`.

## Project Structure

This project is divided into two main parts: the backend and the frontend.

The backend is built with Python and Flask. It handles data processing, analysis, and storage. It also serves the results of the analysis to the frontend.

The frontend is built with React and Vite. It provides a user interface for interacting with the data analysis results.

## Project Architecture

Frontend (React + Vite) <--> Backend (Python + Flask) <--> Database (MongoDB/Mongoose)
                                     |
                                     v
                                  AWS S3 (Dataset Storage)

## Setup

This project consists of a backend and a frontend, each with its own set of dependencies.

### Backend

The backend is a Python application that uses Flask. To set up the backend:

1. Navigate to the `backend` directory.
2. If you haven't already, create a virtual environment: `python3 -m venv venv`
3. Activate the virtual environment:
   - On macOS and Linux: `source venv/bin/activate`
   - On Windows: `.\venv\Scripts\activate`
4. Install the Python dependencies: `pip install -r requirements.txt`

### Frontend

The frontend is a React application that uses Vite. To set up the frontend:

1. Navigate to the `frontend` directory.
2. Install the Node.js dependencies: `npm install`

## Running the Project

### Backend

To run the backend:

1. Make sure you're in the `backend` directory.
2. Make sure the virtual environment is activated.
3. Run the application: `python main.py`

### Frontend

To run the frontend:

1. Navigate to the `frontend` directory.
2. Run the application: `npm run dev`

Remember to deactivate the virtual environment when you're done working on the project: `deactivate` on macOS/Linux, `deactivate.bat` on Windows.

## Testing

Tests are located in the `tests` directories in both the `backend` and `frontend` directories. To run the tests, navigate to the respective directory and run:

```
pytest
```

for the backend, and:

```
npm test
```

for the frontend.

## Contributing

Contributions are welcome. Please submit a pull request or open an issue to discuss your proposed changes.

## License

This project is licensed under the MIT License.

## Contact

For any inquiries or collaboration opportunities, please reach out to me on [LinkedIn](https://www.linkedin.com/in/chayada-s-1a026220/).
