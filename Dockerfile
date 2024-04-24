FROM python
COPY . /app
WORKDIR /app
RUN pip install nltk  
RUN python -m nltk.downloader stopwords punkt
CMD ["python" , "app.py"]