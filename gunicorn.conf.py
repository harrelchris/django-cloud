import multiprocessing

import environ

env = environ.Env()

env.read_env()

HOST = env.str("HOST")

PORT = env.int("PORT")

accesslog = "-"

bind = f"{HOST}:{PORT}"

chdir = "app"

max_requests = 1200

max_requests_jitter = 50

workers = 2 * multiprocessing.cpu_count() + 1

wsgi_app = "core.wsgi:application"
