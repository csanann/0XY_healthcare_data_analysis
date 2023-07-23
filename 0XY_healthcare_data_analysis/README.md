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

To set up this project, you will need to install the required packages for both the backend and the frontend.

For the backend, navigate to the `backend` directory and run:

```
pip install -r requirements.txt
```

For the frontend, navigate to the `frontend` directory and run:

```
npm install
```

## Running the Project

To run the backend, navigate to the `backend` directory and run:

```
python main.py
```

To run the frontend, navigate to the `frontend` directory and run:

```
npm start
```

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

For any inquiries or collaboration opportunities, please reach out to me on 
```
[LinkedIn](https://www.linkedin.com/in/chayada-s-1a026220/).
```