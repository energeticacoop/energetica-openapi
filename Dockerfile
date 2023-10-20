# Use the official Python 3.9 image
FROM python:3.9

# Set the working directory to /code
WORKDIR /code

# Copy the requirements file into the container at /code/requirements.txt
COPY ./requirements.txt /code/requirements.txt

# Install the required packages from requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the entire local ./app directory into the container at /code/app
COPY ./app /code/app

# Set the working directory to /code/app
WORKDIR /code/app

# Start the FastAPI application using uvicorn
CMD ["uvicorn", "main:app", "--reload", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]
