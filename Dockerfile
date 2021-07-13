FROM python:3.9-slim-buster
EXPOSE 5000
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Python venv erstellen
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv ${VIRTUAL_ENV}
ENV PATH="${VIRTUAL_ENV}/bin:$PATH"

# Bibliotheken installieren und Verezeichnis vorbereiten
COPY requirements.txt .
RUN python -m pip install --upgrade pip; \
    python -m pip install -r requirements.txt; \
    python -W ignore -m nltk.downloader -d /usr/local/share/nltk_data punkt; \
    python -m pip install gunicorn; \
    mkdir -p /app/v3/model

WORKDIR /app
COPY . /app

# Benutzerkonto -> Sicherheit (kein root)
RUN useradd appuser && chown -R appuser /app
USER appuser

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "chatbot-webgui:app"]
