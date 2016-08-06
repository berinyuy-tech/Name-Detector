From python:3.7

WORKDIR /usr/src/app

COPY . .

RUN pip install spacy
RUN python -m spacy download en_core_web_sm
RUN pip3 install glob3
