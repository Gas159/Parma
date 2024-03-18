FROM python:3.10.12

SHELL ['/bin/bash', '-c']

# SET  environments variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONINBUFFERED 1

RUN pip install --upgrade pip

RUN apt-get update && apt-get -qy install gcc libjpeg-dev libxslt-dev flake8

RUN useradd -rms /bin/bash gas && chmod 777 /opt /run

WORKDIR  /gas

RUN  mkdir /gas/static && mkdir /gas/media && chown -R gas:gas /yt && chmod 755 /gas

COPY --chown=gas:gas . .

RUN pip install -r requirements.txt

USER gas

CMD ['gunicorn', '-b', '0.0.0.0:8000', 'soaqaz.wsgi:application']