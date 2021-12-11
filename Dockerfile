FROM python:3.9-slim


WORKDIR app/
COPY api/* app/
RUN pip install -r app/requirements.txt
CMD ["uvicorn", "app.index:API", "--host", "0.0.0.0", "--port", "9090"]
