FROM python:3.8-slim

WORKDIR /app
RUN pip install --no-cache-dir pandas numpy pillow

#COPY Create_Cropped_images_main.py Create_Cropped_images_main.py
COPY download_images.py .
COPY download_script.sh .
RUN chmod +x download_script.sh
ENTRYPOINT ["./download_script.sh"]
CMD ["Data/*.csv"]
