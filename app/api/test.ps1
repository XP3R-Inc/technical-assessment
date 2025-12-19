iwr http://127.0.0.1:8000/api/customers -UseBasicParsing |
  Select-Object StatusCode, Content



$body = @{
  cid = 5987
  opportunity_sales_group = "Enterprise AE"
  opportunity_status = "Open"
  monthly_estimated_revenue = 2500.00
  estimated_delivery_date = "2026-03-01"
  non_recurring = "No"
  days_since_last_updated = 0
} | ConvertTo-Json

iwr http://127.0.0.1:8000/api/opportunities `
  -Method POST `
  -ContentType "application/json" `
  -Body $body `
  -UseBasicParsing |
  Select-Object StatusCode, Content


$body = @{ cid = 999999999 } | ConvertTo-Json

iwr http://127.0.0.1:8000/api/opportunities `
  -Method POST `
  -ContentType "application/json" `
  -Body $body `
  -UseBasicParsing |
  Select-Object StatusCode, Content


