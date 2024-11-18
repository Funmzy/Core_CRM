FROM python:3.10


WORKDIR /the/workdir/path

COPY requirements.txt ./

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

EXPOSE 8000

CMD ["fastapi dev", "./src/main.py"]