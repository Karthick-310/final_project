FROM python:3.8.0
WORKDIR /final_project
COPY  . /final_project
RUN /bin/sh -c pip intall -r requirements.txt
EXPOSE 3000
CMD python ./app.py

