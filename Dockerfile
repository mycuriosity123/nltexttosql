FROM python:3.9-slim
COPY  . /app
WORKDIR /app
RUN pip install docker --no-cache -r requirements.txt
EXPOSE 5001 8501
CMD ["/bin/bash", "-c", "gunicorn --bind 0.0.0.0:5001 src.app:app & streamlit run main.py --server.address=0.0.0.0 --server.port=8501"]
