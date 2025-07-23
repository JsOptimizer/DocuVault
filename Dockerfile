FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY instance/__init__.py instance/config.py /instance
COPY . .
EXPOSE 5000
CMD ["flask","--app","flaskr","run","--debug","-h","0.0.0.0"]