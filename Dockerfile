# build the React frontend
FROM node:16.14.2-alpine as frontend-build

WORKDIR /frontend
COPY frontend/package.json ./
COPY frontend/src ./src
COPY frontend/index.html ./
COPY frontend/vite.config.js ./
RUN npm install
RUN npm run build

# build the Flask api backend
FROM python:3.7.16
WORKDIR /app
COPY --from=frontend-build /frontend/dist ./dist
COPY main.py ./main.py

RUN mkdir ./backend
COPY backend/ ./backend
RUN python -m pip install --upgrade pip
RUN pip install -r ./backend/requirements.txt

EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]