# build the React frontend
FROM node:16.14.2-alpine as react-build

WORKDIR /frontend
COPY frontend/package.json ./
COPY frontend/package-lock.json ./
COPY frontend/src ./src

COPY backend/static/index.html ./
COPY frontend/vite.config.js ./
RUN npm install
RUN npm run build

# build the Flask api backend
FROM python:3.7.16
WORKDIR /app
COPY --from=react-build /frontend/dist ./backend/static/dist
COPY main.py ./main.py

COPY main.py ./main.py
COPY backend/ ./backend

RUN python -m pip install --upgrade pip
RUN pip install -r ./backend/requirements.txt

EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:8080", "main:app"]