FROM python:3.9-slim

RUN apt-get update \
    && apt-get -y upgrade \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update \
    && apt-get install -y \
    curl \
    wget \
    && rm -rf /var/lib/apt/lists/*

ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Allow service to handle stops gracefully
STOPSIGNAL SIGQUIT

# Install pipenv
RUN pip3 install pipenv

# Install dependencies
COPY Pipfile* ./

RUN pipenv requirements --dev >dev-requirements.txt

RUN pip install --upgrade pip

RUN pip install -r dev-requirements.txt
# Start the server
ADD . .

CMD gunicorn --bind :8000 giftprojects.wsgi:application

