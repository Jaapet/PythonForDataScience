from datetime import datetime
import time

seconds = time.time()
formatted = f"{seconds:,.4f}"
scientific = f"{seconds:.2e}"
date = datetime.now().strftime("%b %d %Y")

print(f"Seconds since January 1, 1970: {formatted} or {scientific} in scientific notation.")
print(date)