FROM python:3.9-slim



ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Allow service to handle stops gracefully
STOPSIGNAL SIGQUIT

# Install pipenv
RUN pip3 install pipenv

# Install dependencies
COPY Pipfile* ./

RUN pipenv requirements --dev >dev-requirements.txt

RUN pip3 install --upgrade pip

RUN pip3 install -r dev-requirements.txt
# Start the server
ADD . .

CMD gunicorn --bind :8000 giftprojects.wsgi:application

