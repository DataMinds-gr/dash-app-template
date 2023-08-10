# Dash by Plotly App Template

This is a template project for creating web applications using Dash by Plotly. Dash is a powerful Python framework for building interactive web applications with ease. This template provides a basic structure to get you started quickly.

The purpose of this project is to demonstrate different aspects of App Development using Dash by Plotly in an end-to-end manner. The project is structured in a way that it can be used as a template for creating new projects.

> Use the final app as a reference / DEMO for presentation in prospect clients.

## Resources

1. [Dash by Plotly](https://dash.plotly.com/)
2. [Dash Mantine Components](https://www.dash-mantine-components.com/)
3. [Structuring a large Dash application - best practices to follow](https://community.plotly.com/t/structuring-a-large-dash-application-best-practices-to-follow/62739)
4. [Dash App Structure](https://github.com/bradley-erickson/dash-app-structure)

---

## Features

1. How to structure a complex multipage Dash by Plotly App

2. How to use **PyEnv + Poetry** for dependency management

3. How to write and run tests using `pytest`

4. How to use **Dash Mantine Components** and **CSS** to style a Dash App

5. How to setup User Authenication

6. How to setup and use a Database

7. How to **Dockerize** the app and deploy to **GCP**

8. How to setup CI/CD using **GitHub Actions**

9. How to use **Pre-commit**, **Black**, **Flake** and **Isort** for code formatting.

## Use cases

The repository includes sample pages for the following uses cases:

1. Analytics Dashboard
2. Machine Learning Prediction UI
3. Chatbot
4. About Page
5. Contact Page
6. Notifications Functionality

---

## Getting Started

### Using Poetry and Pyenv for Python Dependency Management

1. Install `pyenv` <https://github.com/pyenv/pyenv> and `poetry` <https://python-poetry.org/docs/#installation> on your machine.

2. Install the appropriate Python version:

    ```{bash}
    cd ./dash-app-template
    pyenv install 3.9.16
    pyenv local 3.9.16
    ```

3. Configure Poetry to create the virtual environment in the project root:

    ```{bash}
    poetry config virtualenvs.in-project true
    ```

4. Install all the dependencies with a single command:

    ```{bash}
    poetry install
    poetry lock
    poetry check
    ```

5. Activate the virtual environment

    ```{bash}
    poetry shell
    ```

## Running the App

```{bash}
./run.sh
```
