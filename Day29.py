import pandas as pd
import numpy as np

customers = pd.DataFrame({
    "customer_id":[101,102,103,103,104,105],
    "signup_date":["2024-01-05","2024-02-10","2024-03-01","2024-03-01","2024-03-15","2024-03-20"],
    "segment":["Retail","SMB","Enterprise","Enterprise","Retail",None],
    "plan":["Monthly","Annual","Monthly","Monthly","Monthly","Monthly"]
})

usage = pd.DataFrame({
    "customer_id":[101,101,102,103,104,104,105],
    "date":["2024-05-01","2024-06-01","2024-06-15","2024-05-20","2024-05-10","2024-07-20","2024-05-22"],
    "logins":[5,2,8,0,10,1,4],
    "minutes_used":[120,55,240,0,350,30,90]
})

billing = pd.DataFrame({
    "customer_id":[101,101,102,103,104,105,105],
    "bill_date":["2024-06-01","2024-07-01","2024-07-01","2024-06-01","2024-06-01","2024-05-01","2024-06-01"],
    "amount":[49.0,49.0,490.0,49.0,49.0,49.0,49.0],
    "paid":[True,False,True,True,True,True,False],
    "pay_method":["Card","Card","UPI","Card","Wallet","Card","Card"]
})


customers["signup_date"] = pd.to_datetime(customers["signup_date"])
usage["date"] = pd.to_datetime(usage["date"])
billing["bill_date"] = pd.to_datetime(billing["bill_date"])
customers["segment"] = customers["segment"].str.strip().str.lower()
customers["plan"] = customers["plan"].str.strip().str.lower()
customers = customers.sort_values(["customer_id","signup_date"]).drop_duplicates(subset = ["customer_id"], keep="last")
usage = usage.drop_duplicates()
billing = billing.drop_duplicates()
