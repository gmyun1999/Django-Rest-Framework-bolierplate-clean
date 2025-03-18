import os
import subprocess
import sys
import platform
import secrets

# Constants for dependencies
MINIMUM_DEPENDENCIES = {
    "Django": "5.0.6",
    "djangorestframework": "3.15.2",
    "django-environ": "0.11.2",
    "django-dotenv": "1.4.2",
    "pydantic": "2.7.4",
    "django-cors-headers": "4.4.0",
    "dacite": "1.8.1",
    "arrow": "1.3.0",
}

DEVELOPMENT_DEPENDENCIES = {
    "mypy": "1.11.2",
    "pre-commit": "3.8.0",
    "whitenoise": "6.8.2",
    "psycopg2-binary": "2.9.10",
    "pymysql": "1.1.1",
    "types-pymysql": "1.1.0.20240524",
    "httpx": "0.27.2",
    "ulid-py": "1.1.0",
    "jinja2": "3.1.4",
    "asgiref": "3.8.1",
    "django-cte": "1.3.3",
    "django-extensions": "3.2.3",
    "pydot": "3.0.2",
    "gunicorn": "23.0.0",
    "drf-yasg": "1.21.8",
    "drf-spectacular": "0.27.2",
    "boto3": "1.35.72",
}

def generate_secret_key():
    return secrets.token_urlsafe(50)

def create_env_file():
    secret_key = generate_secret_key()

    # 최종 프로젝트 디렉토리를 현재 작업 디렉토리로 지정
    project_root = os.getcwd()

    env_files = {
        ".env": f"ENV=\nSECRET_KEY={secret_key}\nALLOWED_HOSTS=\nDB_PASSWORD=\nDB_HOST=\n",
        ".local.env": f"ENV=localhost\nSECRET_KEY={secret_key}\nALLOWED_HOSTS=\nDB_PASSWORD=\nDB_HOST=\n",
        ".prod.env": f"ENV=prod\nSECRET_KEY={secret_key}\nALLOWED_HOSTS=\nDB_PASSWORD=\nDB_HOST=\n"
    }
    for file, content in env_files.items():
        file_path = os.path.join(project_root, file)
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"{file} env file created: {file_path}")
        except Exception as e:
            print(f"{file} 파일 생성 중 오류 발생: {e}")

def display_dependencies(dependencies):
    print("\nPlanned Dependencies:")
    for i, (name, version) in enumerate(dependencies.items(), start=1):
        print(f"{i}. {name}=={version}")

def update_dependency_version(dependencies):
    while True:
        display_dependencies(dependencies)
        choice = input("Enter the number of the dependency to change or 'done' to proceed: ").strip()
        if choice.lower() == 'done':
            break
        if not choice.isdigit() or int(choice) not in range(1, len(dependencies) + 1):
            print("Invalid choice. Please enter a valid number.")
            continue

        dep_index = int(choice) - 1
        dep_name = list(dependencies.keys())[dep_index]
        new_version = input(f"Enter the new version for {dep_name}: ").strip()
        dependencies[dep_name] = new_version

def confirm_and_install_dependencies(dependencies):
    display_dependencies(dependencies)
    choice = input("Do you want to install these dependencies? (y/n): ").strip().lower()
    if choice != 'y':
        print("Dependency installation aborted.")
        sys.exit(0)

def generate_requirements(dependencies):
    with open("requirements.txt", "w") as f:
        for name, version in dependencies.items():
            f.write(f"{name}=={version}\n")

def install_poetry():
    try:
        subprocess.run(["poetry", "--version"], check=True)
        print("Poetry is already installed.")
    except FileNotFoundError:
        choice = input("Poetry is not installed. Would you like to install it now? (y/n): ").strip().lower()
        if choice != 'y':
            print("Skipping Poetry installation.")
            return
        print("Installing Poetry...")
        os_name = platform.system()
        if os_name == "Windows":
            # Use PowerShell for installation on Windows
            subprocess.run(["powershell", "-Command", "(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -"], check=True)
        elif os_name == "Darwin":  # macOS
            subprocess.run(["curl", "-sSL", "https://install.python-poetry.org", "|", "python3", "-"], check=True)
        else:
            print(f"Unsupported OS: {os_name}")
            sys.exit(1)
        print("Poetry installation completed.")

def install_pipenv():
    try:
        subprocess.run(["pipenv", "--version"], check=True)
        print("Pipenv is already installed.")
    except FileNotFoundError:
        print("Pipenv is not installed. Installing now...")
        subprocess.run([sys.executable, "-m", "pip", "install", "pipenv"], check=True)
        print("Pipenv installation completed.")

def handle_dependency_tool():
    print("Do you want to install:")
    print("1. Minimum Dependencies")
    print("2. Minimum + Development Dependencies")
    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == "1":
        selected_dependencies = MINIMUM_DEPENDENCIES.copy()
    elif choice == "2":
        selected_dependencies = {**MINIMUM_DEPENDENCIES, **DEVELOPMENT_DEPENDENCIES}
    else:
        print("Invalid choice. Exiting.")
        sys.exit(1)

    print("\nReview and modify dependencies if necessary.")
    update_dependency_version(selected_dependencies)

    tool = "{{ cookiecutter.dependency_tool }}"
    try:
        if tool == "1 (pip)":
            print("Using pip. Generating requirements.txt...")
            confirm_and_install_dependencies(selected_dependencies)
            generate_requirements(selected_dependencies)
            subprocess.run(["pip", "install", *[f"{name}=={version}" for name, version in selected_dependencies.items()]], check=True)
        elif tool == "2 (poetry)":
            print("Using Poetry. Setting up pyproject.toml...")
            install_poetry()
            if not os.path.exists("pyproject.toml"):
                subprocess.run(["poetry", "init", "--no-interaction"], check=True)
            subprocess.run(["poetry", "add"] + [f"{name}=={version}" for name, version in selected_dependencies.items()], check=True)
        elif tool == "3 (pipenv)":
            print("Using Pipenv. Setting up Pipfile...")
            install_pipenv()
            confirm_and_install_dependencies(selected_dependencies)
            generate_requirements(selected_dependencies)
            subprocess.run(["pipenv", "install"] + [f"{name}=={version}" for name, version in selected_dependencies.items()], check=True)
        else:
            print(f"Unknown dependency tool: {tool}")
            sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"Error during dependency installation: {e}")
        print("Installation halted. Check the error message above for details.")
        sys.exit(1)

if __name__ == "__main__":
    if "{{ cookiecutter.dependency_tool }}" != "4 (None)":
        handle_dependency_tool()
    create_env_file()
    print("Project setup completed.")