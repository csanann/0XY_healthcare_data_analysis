FROM python:3.9.16

WORKDIR backend/

COPY backend/requirements.txt .
RUN pip install -r requirements.txt

COPY backend/ .

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]