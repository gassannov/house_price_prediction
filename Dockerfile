FROM python:3.10-slim-bullseye
RUN python3 -m pip install --upgrade pip

COPY . ./project


WORKDIR /project

EXPOSE 8000
RUN pip3 install -r requirements.txt
WORKDIR /project
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]