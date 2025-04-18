# 1. Python imajını kullan
FROM python:3.10-slim

# 2. Çalışma dizinini oluştur
WORKDIR /app

# 3. Dosyaları konteynera kopyala
COPY . /app

# 4. Kütüphaneleri yükle
RUN pip install --no-cache-dir -r requirements.txt

# 5. Bot'u başlat
CMD ["python", "bot.py"]
