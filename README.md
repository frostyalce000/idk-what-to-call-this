# idk-what-to-call-this

A monorepo for a trading-strategies project with a Streamlit frontend and a FastAPI backend backed by PostgreSQL.

## Project structure

```
├── app/          # Streamlit frontend (deployed as py-strats on Fly.io)
├── server/       # FastAPI backend + database layer (deployed as py-strats-server on Fly.io)
└── .github/      # CI workflows for Fly.io deployments
```

## Tech stack

| Component | Stack |
|-----------|-------|
| Frontend | Python 3.12, Streamlit |
| Backend | Python 3.12, FastAPI, SQLAlchemy, Uvicorn |
| Database | PostgreSQL (with pgvector extension for local Docker setup) |
| Deployment | [Fly.io](https://fly.io) |

## Prerequisites

- Python 3.12
- [flyctl](https://fly.io/docs/hands-on/install-flyctl/) (for deployment)
- Docker and Docker Compose (optional, for local PostgreSQL)

## Local development

### Frontend (`app/`)

```bash
cd app
pip install -r requirements.txt
streamlit run src/main.py
```

The app runs at [http://localhost:8501](http://localhost:8501).

### Backend (`server/`)

1. Set the `DATABASE_URL` environment variable (or add it to a `.env` file in `server/`):

   ```
   DATABASE_URL=postgresql+psycopg2://<user>:<password>@localhost:5621/<db_name>
   ```

2. Install dependencies and start the server:

   ```bash
   cd server
   pip install -r requirements.txt
   python -m src.main
   ```

The API runs at [http://localhost:8080](http://localhost:8080).

### Local PostgreSQL (optional)

From the `server/` directory, start a Postgres container with Docker Compose:

```bash
cd server
# Create a .env file with POSTGRES_USER, POSTGRES_PASSWORD, and POSTGRES_DB
docker compose up -d
```

Postgres is exposed on host port **5621**. See [server/README.md](server/README.md) for Fly.io Postgres setup and management.

### Seed sample data

```bash
cd server
python scripts/add_to_db.py
```

## API endpoints

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/` | Health check |
| `GET` | `/database` | Test database connectivity |
| `GET` | `/api/price/` | Fetch price data (currently queries AAPL, 1-minute timeframe) |

## Deployment

Both apps deploy to Fly.io via GitHub Actions on pushes to `main`:

- **`app/`** changes → deploy frontend (`py-strats`)
- **`server/`** changes → deploy backend (`py-strats-server`)

Deployments require a `FLY_API_TOKEN` secret in the repository settings.

Manual deployment:

```bash
# Frontend
cd app && flyctl deploy

# Backend
cd server && flyctl deploy
```

## Environment variables

| Variable | Used by | Description |
|----------|---------|-------------|
| `DATABASE_URL` | `server/` | PostgreSQL connection string |
| `POSTGRES_USER` | Docker Compose | Local Postgres username |
| `POSTGRES_PASSWORD` | Docker Compose | Local Postgres password |
| `POSTGRES_DB` | Docker Compose | Local Postgres database name |
