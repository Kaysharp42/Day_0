from datetime import datetime

current_date = datetime.now()
d= datetime(1970, 1, 1)
diff = (current_date - d).total_seconds()
print(f"Second since {d.strftime("%B %d %Y")}: {diff} or {diff:.2e} in scientific notation")
print(current_date.strftime("%b %d %Y"))