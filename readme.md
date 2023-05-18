чтобы собрать докер:
docker build -t house_inference .  
 
чтобы запустить докер:
docker run -p 8000:8000 --name house_inference house_inference

потом можно отправлять запросы
посмотреть как отправлять запросы можно в requests.py
