## 📄 **`README.md`**

````markdown
# Text2SQL Project
자연어 문장을 SQL 쿼리로 변환하는 Streamlit 기반 앱
이 프로젝트는 [Poetry](https://python-poetry.org/)를 사용하여 Python 의존성과 가상환경을 관리하며, LangGraph 및 LangChain 기반 AI 에이전트를 구현합니다.

---

## ✅ 설치 및 환경 구성

### 1️⃣ 가상환경 설치

Poetry

```bash
curl -sSL https://install.python-poetry.org | python3 -

poetry install
poetry shell

````

Python venv:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

### 2️⃣ 프로젝트 실행

프로젝트 루트 디렉토리(`Makefile`이 위치한 곳)에서 아래 명령어 실행:

```bash
# 모든 서비스 실행 (PostgreSQL + 앱 빌드/실행)
make up

# 모든 서비스 종료 (앱 + PostgreSQL)
make down
---

접속: http://localhost:8501

### 3️⃣ 📁 Project Folder Structure

```plaintext
```
├── app
│   ├── app.py
│   ├── __init__.py
│   ├── pages
│   │   ├── business_rules.py
│   │   ├── examples.py
│   │   ├── knowledge_base.py
│   │   ├── playground.py
│   │   ├── settings.py
│   │   └── sql_instructions.py
│   └── utils.py
├── descriptors
│   └── default
│       └── t2sql_descriptor.json
├── Dockerfile
├── init-db.sh
├── main.py
├── Makefile 
├── poetry.lock
├── pyproject.toml
├── README.md
├── requirements.txt
├── run.sh
└── t2sql
    ├── agent.py
    ├── base.py
    ├── controller
    │   ├── ingest_documentation.py
    │   ├── __init__.py
    │   └── make_answer.py
    ├── ingestors
    │   ├── __init__.py
    │   └── text_document_ingestor.py
    ├── __init__.py
    ├── prompts.py
    ├── sql
    │   ├── client.py
    │   └── __init__.py
    ├── types
    │   └── __init__.py
    ├── utils.py
    └── vectordb
        ├── base.py
        ├── chromadb.py
        └── __init__.py
```

