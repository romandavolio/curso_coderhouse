from datetime import datetime, timedelta

dto = datetime.now()

dt = datetime(2022, 12, 10)

restante = dt - dto

print(restante.total_seconds())