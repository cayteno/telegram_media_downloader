FROM python:3.11.2-alpine As compile-image

WORKDIR /app

COPY requirements.txt /app/

RUN apk add --no-cache --virtual .build-deps gcc musl-dev \
    && pip install --trusted-host pypi.python.org -r requirements.txt \
    && apk del .build-deps && rm -rf requirements.txt

RUN apk add --no-cache ca-certificates && \
    wget https://downloads.rclone.org/rclone-current-linux-amd64.zip && \
    unzip rclone-current-linux-amd64.zip && \
    mv rclone-*-linux-amd64 rclone && \
    rm rclone-current-linux-amd64.zip \
    chmod +x rclone \
    rclone version

FROM python:3.11.2-alpine As runtime-image

ENV PATH=$PATH:/app/rclone

WORKDIR /app

COPY --from=tangyoha/telegram_media_downloader_compile:latest /app/rclone /app/rclone

COPY --from=tangyoha/telegram_media_downloader_compile:latest /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages

COPY config.yaml data.yaml setup.py media_downloader.py /app/
COPY module /app/module
COPY utils /app/utils

CMD ["python", "media_downloader.py"]
