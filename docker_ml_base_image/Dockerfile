FROM relevolab/miniconda:latest
RUN apt update
RUN apt -y install libgl1-mesa-glx
RUN pip install --upgrade pip
COPY /docker_ml_base_image/requirements.txt .
RUN pip install -r requirements.txt
COPY /application .

ENV PYTHONPATH="${PYTHONPATH}:/app/application"

WORKDIR /src

CMD ["python3.6", "app.py"]