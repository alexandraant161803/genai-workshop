FROM python:3.11 as BUILD

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt

RUN pip install --user -r requirements.txt

FROM python:3.11-slim as RUN

RUN apt-get update

WORKDIR /usr/src/app

COPY --from=BUILD /root/.local /root/.local

COPY . .

RUN pip install -e .
ENV PATH=/root/.local/bin:$PATH
RUN playwright install && playwright install-deps

CMD uvicorn gen_ai_workshop_api.main:app --host 0.0.0.0 --port 8000