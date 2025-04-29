FROM python:3.11-slim

# set workdir
WORKDIR /app

# install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
  && rm -rf /var/lib/apt/lists/*

# copy & install python deps
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# copy application
COPY . .

# create instance folder for SQLite
RUN mkdir -p instance

EXPOSE 5000
ENV FLASK_APP=app
ENV FLASK_ENV=production

CMD ["flask", "run", "--host=0.0.0.0"]