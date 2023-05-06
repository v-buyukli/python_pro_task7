import time

from university.models import RequestLog


class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path
        method = request.method

        start_time = time.time()
        response = self.get_response(request)
        execution_time = time.time() - start_time

        with open("log.txt", "a") as f:
            f.write(f"{path}, {method}, {execution_time}\n")

        RequestLog.objects.create(path=path, method=method, execution_time=execution_time)

        return response
