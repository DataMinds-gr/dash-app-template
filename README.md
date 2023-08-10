# Dash by Plotly App Template

This is a template project for creating web applications using Dash by Plotly. Dash is a powerful Python framework for building interactive web applications with ease. This template provides a basic structure to get you started quickly.

## Resources

1. [Dash by Plotly](https://dash.plotly.com/)
2. [Dash Mantine Components](https://www.dash-mantine-components.com/)
3. [Structuring a large Dash application - best practices to follow](https://community.plotly.com/t/structuring-a-large-dash-application-best-practices-to-follow/62739)
4. [Dash App Structure](https://github.com/bradley-erickson/dash-app-structure)

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
