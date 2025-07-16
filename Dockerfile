# base image
FROM python:3.11

# workdir
WORKDIR /personality_pred

#copy and install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#Copy rest of application
COPY . .

#port
EXPOSE 8000

#command
CMD ["uvicorn","app:app","--host","0.0.0.0","--port","8000"]
