FROM python:3.11-slim

# Create user and environment
RUN groupadd --gid 1000 appuser \
    && useradd --uid 1000 --gid 1000 -ms /bin/bash appuser

# 설치 필수 도구
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    git \
    libpq-dev \
    curl

# pip 및 virtualenv 업그레이드
RUN pip install --upgrade pip virtualenv

USER appuser
WORKDIR /home/appuser

# 프로젝트 전체 복사
COPY . .

# 가상환경 생성 및 requirements 설치
ENV VIRTUAL_ENV=/home/appuser/venv
RUN virtualenv ${VIRTUAL_ENV} \
    && ${VIRTUAL_ENV}/bin/pip install --upgrade pip \
    && ${VIRTUAL_ENV}/bin/pip install -r requirements.txt

# Streamlit 포트
EXPOSE 8501

# 실행 파일 권한 부여 및 권한 설정
USER root
RUN chmod +x /home/appuser/run.sh \
    && chown -R appuser:appuser /home/appuser
USER appuser

# 앱 실행
ENTRYPOINT ["./run.sh"]
