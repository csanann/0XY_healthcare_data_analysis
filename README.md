
# The 0XY_Healthcare Data Analysis Project

This project is a learning exercise aimed at analyzing healthcare data with a focus on patient demographics, disease types, treatment types, and treatment outcomes. The goal is to gain a better understanding of the factors that contribute to successful treatment outcomes and to identify areas where healthcare provision could potentially be improved.

## Disclaimer

This project is for learning purposes only. The data used is publicly available and does not contain any sensitive or personal health information.

## Dataset

The data for this project is sourced from the [Patient Treatment Classification | Kaggle](https://www.kaggle.com/datasets/saurabhshahane/patient-treatment-classification).

## Tech/Tools

- Data Analysis: Python (pandas, NumPy, matplotlib, seaborn, scikit-learn)
- Data Storage: MongoDB/Mongoose
- Deployment: Docker, AWS EC2
- Version Control: Git, Github
- Backend: Python, Flask, Gunicorn
- Front-end Interface: React and Vite
- TDD, BDD: pytest for unit tests, integration tests, and functional tests. BDD: BDD framework like `behave` or `pytest-bdd`. Code coverage is measured with `pytest-cov`.
- Continuous Integration/Continuous Deployment (DI/CD): GitHub Action

## Project Structure

This project is divided into two main parts: the backend and the frontend.

The backend is built with Python, Flask and Gunicorn. It handles data processing, analysis, and storage. It also serves the results of the analysis to the frontend.

The frontend is built with React and Vite. It provides a user interface for interacting with the data analysis results.

## Project Architecture

Frontend (React + Vite) <--> Backend (Python + Flask + Gunicorn) <--> Database (MongoDB/Mongoose)
                                     |
                                     v
                                  AWS S3 (Dataset Storage)

## Setup

This project consists of a backend and a frontend, each with its own set of dependencies.

## Backend Setup

1. Install Docker: Follow the instructions [here](https://docs.docker.com/get-docker/)
3. Navigate to the project directory.
4. build the Docker image: `docker build -t my-python-app .`
5. Run the Docker container: `docker run -p 8080:5000 my-python-app`

### Frontend

1. Navigate to the `frontend` directory.
2. Install the Node.js dependencies: `npm install`
3. Run the application: `npm run dev`

## Running the Project

### Backend

To run the backend:

1. Make sure you're in the project directory.
2. Build the Docker image: `docker build -t my-python-app .`
3. Run the Docker container: `docker run -p 8080:5000 my-python-app`

### Frontend

To run the frontend:

1. Navigate to the `frontend` directory.
2. Run the application: `npm run dev`

## Testing

Tests are located in the `tests` directories in both the `backend` and `frontend` directories. 
To run the tests, navigate to the respective directory and run:

```
pytest
```

for the backend, and:

```
npm test
```

for the frontend.

## Continuous Integration/Continuous Deployment (CI/CD)

We use GitHub Actions for our CI/CD pipeline. This help us automate our software development practices with configuration files and workflows that you can set up in your repository.

## Contributing

Contributions are welcome. Please submit a pull request or open an issue to discuss your proposed changes.

## License

This project is licensed under the MIT License.

## Contact

For any inquiries or collaboration opportunities, please reach out to me on [LinkedIn](https://www.linkedin.com/in/chayada-s-1a026220/).
