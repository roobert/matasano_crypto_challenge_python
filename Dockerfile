FROM python:3.7.4-alpine3.10

COPY . .

RUN ["apk", "--update", "add", "py-pip", "alpine-sdk"]

RUN ["pip3", "install", "iteration_utilities", "pycryptodome"]

WORKDIR ./bin

CMD ["python", "decrypt_byte_by_byte.py", "--fast"]