# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim-buster

RUN mkdir /app

# Install SCIP requirements
RUN apt-get update && apt-get install -y wget libgfortran4 libblas3 liblapack3 libtbb-dev libgsl-dev libboost-all-dev build-essential g++ python-dev autotools-dev libicu-dev build-essential libbz2-dev libgmp3-dev libreadline-dev 
RUN wget https://www.scipopt.org/download/release/SCIPOptSuite-7.0.1-Linux.sh -O scip.sh && chmod +x scip.sh && ./scip.sh --skip-license && mv bin/scip /app/scip

VOLUME ["/app"]
ADD . /app/
WORKDIR /app

# Install pip requirements
RUN python -m pip install -r requirements.txt

ADD . /app/

# Switching to a non-root user, please refer to https://aka.ms/vscode-docker-python-user-rights
RUN useradd appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
ENTRYPOINT ["python", "run.py"]

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

# Hypixel API key
ENV API_KEY key

# Bot Discord token
ENV DISCORD_TOKEN token
