FROM python:3.7-slim-buster
RUN apt-get update && apt-get install -y git
RUN git clone https://github.com/nir800/VanillaLogin.git
WORKDIR /Vanilla-ISE/
copy requirements.txt  .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "app.py"]
