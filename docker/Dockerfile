FROM  python:3.7-alpine as builder
COPY ./script/requirements.txt /requirements.txt 
RUN mkdir /install
WORKDIR /install
RUN pip install --prefix=/install -r /requirements.txt


FROM  python:3.7-alpine
COPY --from=builder /install /usr/local
COPY ./script/test.py /app/test.py
WORKDIR /app

ENTRYPOINT ["/bin/python3", "test.py"]
