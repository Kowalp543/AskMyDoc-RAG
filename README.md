# AskMyDoc-RAG

AskMyDoc-RAG is an intelligent document understanding web application designed to help users quickly and easily comprehend their medical documents. Powered by FastAPI, LangChain Retrieval-Augmented Generation (RAG) architecture, and Docker, this project allows users to upload documents, process their content, and ask natural language questions to get clear, jargon-free answers.

---

## Features

- **Document Upload:** Upload medical documents (PDFs, etc.) for processing.
- **RAG-powered Q&A:** Ask questions about uploaded documents using state-of-the-art RAG models.
- **Document Management:** View a list of all uploaded documents with easy navigation.
- **Dockerized:** Run locally with Docker for easy environment setup.
- **CI/CD with GitHub Actions:** Automated testing, linting, formatting, and Docker builds on push or PR.
- **Code Quality:** Integrated with Black (code formatter) and Ruff (linter) for clean, maintainable code.
- **Testing:** Pytest-based tests to ensure application stability.

---

## Tech Stack

- Python 3.11
- FastAPI — Modern, fast web framework
- LangChain — Retrieval-Augmented Generation for NLP
- Docker & Docker Compose — Containerization for easy deployment
- PostgreSQL (optional) — Database backend
- Alembic — Database migrations
- GitHub Actions — Continuous Integration / Continuous Deployment (CI/CD)
- Black & Ruff — Code formatting and linting
- Pytest — Testing framework
- Tailwind CSS — Stylish and responsive UI

---

## Getting Started

### Prerequisites

- Docker and Docker Compose installed (for containerized setup)
- Python 3.11 installed (if running locally without Docker)
- Git installed

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Kowalp543/AskMyDoc-RAG.git
    cd AskMyDoc-RAG

2. Create and activate a virtual environment (optional, for local development):

    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate     # Windows

3. Install dependencies:

    pip install -r requirements.txt

4. Run database migrations:

    alembic upgrade head

5. Run the application locally:

    uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

    Or run with Docker Compose:

    docker-compose up --build

6. Open your browser and navigate to:

    Open your browser at http://localhost:8000