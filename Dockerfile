# 使用官方 Python 映像檔
FROM python:3.10-slim

# 設置工作目錄
WORKDIR /app

# 安裝系統依賴（包括 MySQL 開發庫和 netcat）
RUN apt-get update && \
    apt-get install -y --no-install-recommends default-libmysqlclient-dev build-essential netcat-openbsd && \
    rm -rf /var/lib/apt/lists/*

# 複製 requirements.txt 並安裝 Python 依賴
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 安裝 Pillow
RUN pip install Pillow

# 複製專案檔案
COPY . .

# 設置環境變數
ENV PYTHONUNBUFFERED=1

# 暴露端口
EXPOSE 8000

# 運行 Django 開發伺服器
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]