# Candidate Workflow: Clone, Branch, Configure, and Commit

Follow these steps to get set up quickly and keep your work organized during the assessment.

## 1. Clone the Repository

```bash
git clone https://github.com/XP3R-Inc/technical-assessment.git
cd technical-assessment
```

## 2. Create a Working Branch

Push your work to a uniquely named branch so reviewers can inspect your progress:

```bash
git checkout -b feature/<candidate-lastname>-assessment
```

Commit frequently with descriptive messages:

```bash
git commit -am "Implement customer list challenge"
```

## 3. Set Up Environment Variables

The API reads its configuration from environment variables defined in a `.env` file. Use the credentials provided to you and copy the example file:

```bash
cp .env.example .env             # macOS/Linux
copy .env.example .env           # Windows
```

Open `.env` and fill in the values:

```
APP_NAME=Technical Assessment API
MYSQL_HOST=your-db-host
MYSQL_PORT=3306
MYSQL_USER=provided_username
MYSQL_PASSWORD=provided_password
MYSQL_DB=provided_database
```

Finally, ensure the application can locate the file:

```bash
export ENV_FILE=.env             # macOS/Linux (temporary for the shell)
setx ENV_FILE ".env"             # Windows PowerShell (persistent)
```

## 4. Install Dependencies (Python 3.13)

```bash
python -m venv .venv
source .venv/bin/activate        # macOS/Linux
.\.venv\Scripts\Activate.ps1     # Windows PowerShell
pip install --upgrade pip
pip install -r requirements.txt
```

## 5. Run the API and Commit Work

```bash
uvicorn app.main:app --reload --port 8000
```

While you work:

- Commit incremental progress to your branch.
- Push to origin periodically (`git push -u origin feature/<name>-assessment`).
- Capture sample curl commands or Beekeeper screenshots in your commits or PR.

By the end of the session you should have a branch ready for review that the interviewer can diff during your walkthrough.

