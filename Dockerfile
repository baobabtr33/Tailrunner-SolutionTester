#!/bin/bash
 
FROM  --platform=linux/amd64  python:3.9

# 
WORKDIR /code


COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./src/app /code/app

# 
CMD ["uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "9000", "--workers", "10"]