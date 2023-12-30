FROM python:3.10

WORKDIR /Vccorp_training

COPY ./requirements.txt /Vccorp_training/requirements.txt

RUN pip install --no-cache-dir -r /Vccorp_training/requirements.txt

COPY ./tuan1 /Vccorp_training/tuan1

CMD ["uvicorn", "tuan1.bai2_fastapi:app", "--host", "0.0.0.0", "--port", "8000"]
