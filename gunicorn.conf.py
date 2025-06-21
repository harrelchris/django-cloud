import multiprocessing
import os

HOST = os.getenv("HOST", "0.0.0.0")

PORT = os.getenv("PORT", "8000")

accesslog = "-"

bind = f"{HOST}:{PORT}"

chdir = "app"

max_requests = 1200

max_requests_jitter = 50

workers = 2 * multiprocessing.cpu_count() + 1

wsgi_app = "core.wsgi:application"
