FROM python:3.12.9-alpine
COPY  . /app
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5001 8501
CMD ["sh","-c","uvicorn app:app --host 0.0.0.0 --port 5001 & streamlit run main.py --server.port 8501 --server.address 0.0.0.0"]

