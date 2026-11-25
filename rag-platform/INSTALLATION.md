# Installation Guide

## 1. Prerequisites

Install the following:

- Python 3.12
- PostgreSQL
- pgvector extension
- Git

## 2. Clone the Repository

```bash
git clone <repository-url>
cd rag-platform
```

## 3. Create Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

## 4. Install Python Dependencies

```bash
pip install -r requirements.txt
```

## 5. Database Setup

1. Install PostgreSQL.
2. Create the project database.
3. Install and enable the pgvector extension.
4. Run the SQL scripts from `database/scripts/`.

## 6. Environment Configuration

Create a `.env` file in the project root.

Configure the required database credentials and application settings using `.env.example` as a reference.

## 7. Local LLM Setup

Ollama is used for AI-assisted dataset label review.

1. Download and install [Ollama for Windows](https://ollama.com/download/windows).
2. Verify installation:

```powershell
ollama --version
```

3. Download the model:

```powershell
ollama pull qwen2.5:0.5b
```

4. Run the model:

```powershell
ollama run qwen2.5:0.5b
```

## 8. Verify Installation

Verify Python, database connectivity, required dependencies, and local model inference before running the project.