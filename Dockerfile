FROM docker pull python:3.9.21-slim-bullseye

WORKDIR /Dock

# Install the application dependencies
COPY requirements.txt ./
RUN pip install --upgtade pip
RUN pip install -r requirements.txt

COPY . .


CMD ["pthon3", "-m", "flask", "--app","loan","run","--host=0.0.0.0", "--port", "8080"]