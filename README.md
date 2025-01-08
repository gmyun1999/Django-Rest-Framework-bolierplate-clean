# Django-Rest-Framework-Boilerplate-Clean

클린 아키텍처를 기반으로 Django Rest Framework(DRF) 프로젝트에서 사용할 수 있는 보일러플레이트 코드입니다.  
이 프로젝트는 **Cookiecutter**를 활용해 동적으로 코드를 생성하며, 빠르고 효율적인 프로젝트 초기화를 지원합니다.

---

## 🔧 주요 특징

- 클린 아키텍처 기반의 프로젝트 구조.
- 동적 코드 생성을 위한 **Cookiecutter** 지원.
- 사용자가 선택한 의존성 관리 도구(**pip**, **poetry**, **pipenv**)를 자동으로 설정하고 의존성을 설치.
- 지속적인 버전 업데이트를 통해 최신 기술 스택 지원.

---

## 📥 설치 및 시작하기

### 1. Cookiecutter 설치

먼저 Cookiecutter를 설치합니다:

```bash
pip install cookiecutter
```

### 2. 프로젝트 생성

아래 명령어로 템플릿을 기반으로 프로젝트를 생성합니다:

```bash
cookiecutter https://github.com/your-repo/Django-Rest-Framework-Boilerplate-Clean.git
```

### 3. 입력 값 설정

`cookiecutter` 실행 시 아래와 같은 입력값을 요청받습니다:

- `project_slug`: 설정 파일에 사용할 이름 (예: "macro_be")
- `project_name`: 프로젝트 이름 (예: "macro_be")
- `django_version`: 사용할 Django 버전 (기본값: "5.0.6")
- `db_engine`: 사용할 데이터베이스 (선택지: "1 (PostgreSQL)", "2 (MySQL)", "3 (MongoDB)")
- `dependency_tool`: 의존성 관리 도구 (선택지: "1 (pip)", "2 (poetry)", "3 (pipenv)", "4 (None)")

입력을 완료하면, 선택한 의존성 관리 도구에 따라 필요한 설정 파일(`requirements.txt`, `pyproject.toml`, `Pipfile`)이 생성되며 의존성 설치가 자동으로 완료됩니다.

---

## 🚀 동작 방법

### 1. 데이터베이스 마이그레이션

생성된 프로젝트 폴더로 이동한 후, 데이터베이스를 초기화합니다:

```bash
python manage.py migrate
```

### 2. 서버 실행

개발 서버를 시작합니다:

```bash
python manage.py runserver
```

---

## 📦 의존성

템플릿은 다음과 같은 주요 패키지를 포함합니다:

### 최소 의존성

- **Django**: 5.0.6
- **Django Rest Framework**: 3.15.2
- **python-decouple**: 0.11.2
- **django-dotenv**: 1.4.2
- **pydantic**: 2.7.4
- **django-cors-headers**: 4.4.0
- **dacite**: 1.8.1
- **arrow**: 1.3.0

### 개발 의존성 (선택 사항)

- **mypy**: 1.11.2
- **pre-commit**: 3.8.0
- **whitenoise**: 6.8.2
- **psycopg2-binary**: 2.9.10
- **pymysql**: 1.1.1
- **jinja2**: 3.1.4
- **gunicorn**: 23.0.0
- **drf-spectacular**: 0.27.2
- **boto3**: 1.35.72

---

## 🔄 버전 관리

보일러플레이트는 정기적으로 업데이트됩니다. 새로운 버전을 받으려면 GitHub에서 최신 코드를 가져오세요:

```bash
git pull origin main
```

---

## 📖 추가 정보

- [Django 공식 문서](https://docs.djangoproject.com/)
- [Django Rest Framework 문서](https://www.django-rest-framework.org/)
- [Cookiecutter 공식 문서](https://cookiecutter.readthedocs.io/)

---

이 보일러플레이트는 Django Rest Framework 프로젝트를 빠르게 시작하고 클린 아키텍처를 기반으로 유지보수를 쉽게 하기 위한 목적으로 설계되었습니다. 😊
