FROM python:3.9.1

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt ; exit 0

WORKDIR /app2

RUN python -m spacy download en_core_web_md


#RUN apt-get install libsndfile1

RUN apt-get -y update

RUN apt-get install -y sox

RUN apt-get install -y libsndfile-dev

RUN apt-get install ffmpeg -y

COPY . .

EXPOSE 8501

CMD streamlit run app_streamlit.py
