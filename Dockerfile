FROM python:3.10 AS builder

MAINTAINER KinKenCode (NotWorkingCode)
LABEL version="1.0"
LABEL description="BH Music telegram bot image."

# Download all dependencies
COPY dependencies.txt .
RUN pip install --user -r dependencies.txt

# Light version from app
FROM python:3.10-slim

WORKDIR /application
COPY --from=builder /root/.local /root/.local
COPY . .

ENV PATH=/root/.local:$PATH

CMD ["python", "-u", "startup.py"]
