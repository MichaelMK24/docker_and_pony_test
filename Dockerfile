FROM python:3.10

WORKDIR /app

# Copy the entire project directory into the container
COPY . /app

# Install any required dependencies
RUN pip install -r requirements.txt

CMD ["python", "repositoryy/repository_user.py"]
