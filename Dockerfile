FROM python:2.7-alpine

ENV FREQUENCY "daily"

WORKDIR /root/docker_ebooks

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x ebooks.py

CMD ln -s /root/docker_ebooks/ebooks.py /etc/periodic/$FREQUENCY/ebooks \
  && python ebooks.py \
  &&  crond -f | grep $FREQUENCY
