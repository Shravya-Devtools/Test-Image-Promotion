FROM alpine:3.18
RUN apk add --no-cache python3
WORKDIR /app
COPY app.py .
EXPOSE 8080
CMD ["python3", "app.py"]
