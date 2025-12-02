# Viewing Assessment Data with Beekeeper Studio

After installing Beekeeper Studio, use this guide to connect to the MySQL
database and inspect the `customer` and `crm_opportunities` tables that power
the interview challenges.

## 1. Create a New Connection

1. Open Beekeeper Studio.
2. Click **New Connection** → **MySQL**.
3. Fill in the fields:
   - **Connection Name:** e.g., `XP3R Assessment`
   - **Host:** value from `MYSQL_HOST`
   - **Port:** `MYSQL_PORT` (default `3306`)
   - **Username:** `MYSQL_USER`
   - **Password:** `MYSQL_PASSWORD`
   - **Database:** `MYSQL_DB`
4. (Optional) Click **Test Connection** to confirm credentials.
5. Save the connection so you can reopen it quickly during the interview.

## 2. Browse Tables

Once connected, the left sidebar lists the available schemas and tables.

- Expand your database -> Tables -> double-click `customer` to open a data tab.
- Repeat for `crm_opportunities`.

Use the built-in filter/search to quickly inspect rows.

## 3. Run SQL Queries

Open a new query tab (`Ctrl/Cmd + N`) and run ad-hoc SQL to validate assumptions.
Example queries:

```sql
-- Verify seeded customers
SELECT CID, Area, Customer_Type FROM customer LIMIT 20;

-- Confirm opportunities exist for a specific customer
SELECT OID, CID, Opportunity_Status
FROM crm_opportunities
WHERE CID = 123
ORDER BY Estimated_Delivery_Date DESC;
```

These queries help the interviewee validate their API responses or craft JOINs
if you extend the exercise.

## Troubleshooting Tips

- If you cannot connect, ensure the database host allows inbound connections
  from your IP (update security groups or firewall rules).
- Double-check the `ENV_FILE` values—Beekeeper should use the same credentials
  FastAPI uses.
- SSL: if the RDS instance enforces SSL, toggle **Use SSL** and provide the CA
  bundle if required.

