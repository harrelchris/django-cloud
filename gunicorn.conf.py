import multiprocessing

accesslog = "-"
bind = "0.0.0.0:8000"
chdir = "app"
max_requests = 1200
max_requests_jitter = 50
workers = 2 * multiprocessing.cpu_count() + 1
wsgi_app = "core.wsgi:application"
