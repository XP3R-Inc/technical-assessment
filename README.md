# Technical Assessment Backend

Python FastAPI backend used to evaluate how candidates design database-backed APIs. The service boots successfully but exposes two unfinished endpoints that the interviewee must complete during the exercise.

## Requirements (What you need installed)

- Python 3.13 (or newer) plus `pip`
- Ability to create a virtual environment (`python -m venv`)
- Git (required; you will need to clone this repository and build on it)
- Network access to a MySQL 8.x database (we will provide AWS RDS configuration values at the interview start)

## Required Git / .env Workflow

Every candidate should follow the steps in `docs/workflow.md`:

- Clone the repository and create a personal feature branch such as `feature/<lastname>-assessment`.
- Copy `.env.example` to `.env`, fill in the credentials you provide, and export `ENV_FILE` so the FastAPI app can load the file.
- Install dependencies with Python 3.13 inside a virtual environment, then run `uvicorn app.main:app --reload --port 8000`.
- Commit frequently, push to origin, and be ready to share the branch or PR at the end of the session.

## Configuration

All configuration is driven by environment variables that can be stored in an `.env` file. The application looks for that file via the `ENV_FILE` environment variable (defaults to `.env` in the repo root).

| Variable         | Description                                               |
| ---------------- | --------------------------------------------------------- |
| `APP_NAME`       | Display name shown in the FastAPI docs                    |
| `ENVIRONMENT`    | Free-form label (`local`, `staging`, etc.)                |
| `MYSQL_HOST`     | MySQL hostname or RDS endpoint                            |
| `MYSQL_PORT`     | MySQL port (default 3306)                                 |
| `MYSQL_USER`     | Username with access to the schema                        |
| `MYSQL_PASSWORD` | Password for the MySQL user                               |
| `MYSQL_DB`       | Database/schema name                                      |
| `ECHO_SQL`       | Set to `true` to log every SQL statement (debugging aid)  |

## Setup & Running Locally

1. **Create and activate a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate        # macOS/Linux
   .\.venv\Scripts\activate         # Windows PowerShell
   ```
   Ensure `python --version` reports **3.13.x** before creating the virtual environment so the dependencies install correctly.
2. **Install dependencies**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```
3. **Create an env file and point the app at it**
   ```bash
   cp .env.example .env             # macOS/Linux
   copy .env.example .env           # Windows
   export ENV_FILE=.env             # macOS/Linux
   setx ENV_FILE ".env"             # Windows PowerShell
   ```
   Fill in the credentials for the MySQL instance that will host the interview schema.

4. **Start the API**
   ```bash
   uvicorn app.main:app --reload --port 8000
   ```
   The interactive docs are available at `http://localhost:8000/docs`.

### (Optional) Inspecting the Data with Beekeeper Studio

If the interviewee prefers a GUI to validate query results, point them to the new Beekeeper docs:

- `docs/beekeeper_install.md` explains how to download and install the tool.
- `docs/beekeeper_view_data.md` covers creating a MySQL connection, browsing the
  `customer` / `crm_opportunities` tables, and running SQL queries.

Use the same credentials stored in `.env` when configuring Beekeeper Studio.

## Verifying the Server

Use `curl` or a browser to confirm the service is up. Both challenge endpoints currently return `501 Not Implemented` until the interviewee writes the logic.

```bash
# Expect 501 with challenge instructions in the response
curl -i http://localhost:8000/api/customers

# Expect 501 from the opportunity endpoint as well
curl -i -X POST http://localhost:8000/api/opportunities \
  -H "Content-Type: application/json" \
  -d '{ "cid": 1 }'
```

For a quick Python smoke test:

```bash
python - <<'PY'
import requests
resp = requests.get("http://localhost:8000/api/customers", timeout=5)
print(resp.status_code, resp.json())
PY
```

## Assessment Overview

- **Duration:** 1.5 hours of hands-on work followed by a 30‑minute readout with the interviewer.
- **Deliverables:** working API endpoints plus a concise summary that explains assumptions, edge cases, and next steps. Candidates can demo directly from their IDE, browser, or any presentation medium they prefer.
- **Scoring rubric:** Completeness of functionality, quality of the solution (tests, error handling, data validation), and clarity of communication during the walkthrough.

Reminder that we value narrative.

### What You Receive

- This FastAPI repository with two partially implemented endpoints and ORM models.
- MySQL credentials that mirrors the Excel workbook provided in the original data case.
- Optional tooling docs (e.g., Beekeeper Studio) to visualize the dataset.

### What You’re Expected to Deliver

- Working implementations for the customer read API and opportunity write API (details below) that compile and run locally.
- A concise summary of findings and next steps that you can walk through live in the post-assessment presentation.
- Talking points on validation, error handling, and any trade-offs you made because of time constraints.

## Business Context – IntraSoft Case

IntraSoft is an enterprise software vendor serving customers across Europe with multiple subscription offerings (accounting, time entry, etc.). Sales teams pair Account Executives with Technical Specialists because implementations are complex. Opportunities are tracked in a CRM along with estimated monthly revenue and expected completion dates. IntraSoft organizes the European business into Areas (France, Germany, Switzerland, Netherlands, UK) and sets revenue targets per Area at the start of each fiscal year (July–June).

Sales leadership is midway through FY2025 (December) and needs an internal CRM prototype that helps them sanity-check data quality and act on the pipeline. The interviewee’s API work enables product teams to:

- Pull a reliable list of customers (with team assignments and commercial flags) so new CRM features have accurate reference data.
- Create or update CRM opportunities programmatically, ensuring every deal is tied to the correct customer ID (CID) and can roll up into revenue forecasts.
- Feed downstream analytics (dashboards, revenue projections, territory health) without manually exporting spreadsheets.

## Dataset Provided

This repo focuses on the first two tables, but the candidate can explore all of them:

1. **Customer** – Unique list of customers (CID) with attributes such as Area, account team assignments, and contract metadata.
2. **CRM Opportunities** – Every in-flight opportunity expected to close by the end of the fiscal year, including estimated monthly revenue.
3. **Revenue Actuals** – Realized subscription revenue by Area (not yet wired into the API but available for reference).
4. **Revenue Targets** – Fiscal-year targets by Area (not yet wired into the API but available for reference).

Customer data is already present in the provided MySQL schema. The `crm_opportunities` table is intentionally empty so the interviewee can seed it
through the POST challenge. We encourage you to use Beekeeper Studio (docs in `docs/`) to verify your inserts as you work.

## Notes Collected From Client

- Product wants a dependable API surface so engineers can read the customer roster and create CRM opportunities without touching SQL directly.
- Data quality matters: every opportunity must reference a valid `CID`, set a status, and include realistic revenue/forecast metadata so downstream dashboards stay accurate.
- Candidates should plan to walk the interviewer through their validation steps (curl, tests, Beekeeper screenshots, etc.) and call out any trade-offs or TODOs they would tackle with more time.
- Documentation is part of the deliverable—share sample requests/responses or brief instructions so another engineer can pick up where you left off.

## Interview Challenges (What the candidate must do)

Both endpoints are wired into the router and raise descriptive `HTTPException`s. The goal is to replace the placeholders with working implementations.

### Challenge 1 – List Customers

- **File:** `app/api/customers.py`, function `list_customers`
- **Supporting code:** `app/models/customer.py`, `app/schemas/customer.py`
- **Requirements:**
  - Use the injected SQLAlchemy session to query every row from the `customer` table (model `Customer`).
  - Return the result serialized by `CustomerRead`.
  - Handle database errors gracefully (raising 500s as needed).

### Challenge 2 – Create an Opportunity

- **File:** `app/api/opportunities.py`, function `create_opportunity`
- **Supporting code:** `app/models/opportunity.py`,
  `app/schemas/opportunity.py`
- **Requirements:**
  - Accept an `OpportunityCreate` payload and persist it to `crm_opportunities`.
  - Ensure the referenced customer (`cid`) exists.
  - Generate a unique `oid` (e.g., `uuid4().hex`) if the database will not supply one.
  - Commit the transaction, refresh the model, and return it as `OpportunityRead`.
  - Roll back and return an appropriate HTTP error if persistence fails.

Discuss validation, error handling, and SQL performance trade-offs during the interview as the candidate works through these tasks.

### Challenge 3 (Bonus) – Build a React UI

**Bonus points** if you can:

- Create a simple React app (using [Vite](https://vitejs.dev/), [Create React App](https://create-react-app.dev/), or any toolchain you prefer).
- Use `fetch` or `axios` to call `GET /api/customers` and display the results in a table.
- The app should show each customer's fields as columns.
- You'll likely need to enable CORS for localhost development (see FastAPI docs or set `--cors` for Uvicorn).
- Submit the code or a link to your project as part of your solution.

This is not required for backend completion, but it's a nice differentiator if you have React skills!

---


## Project Structure

- `app/core/config.py` – loads environment variables and builds the DB URL.
- `app/db/session.py` – SQLAlchemy engine/session factory and dependency.
- `app/models/customer.py` – ORM mapping for the `customer` table.
- `app/models/opportunity.py` – ORM mapping for `crm_opportunities`.
- `app/schemas/customer.py` & `app/schemas/opportunity.py` – Pydantic models.
- `app/api/customers.py` & `app/api/opportunities.py` – challenge endpoints.
- `app/main.py` – FastAPI application factory/entrypoint.