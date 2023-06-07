from locust import TaskSet, task, HttpUser, constant
import random

class TaskTest(TaskSet):

    @task
    def testHttpCat_StatusCode(self):
        res = self.client.get("/201")
        print("Getting 201 cat")

    @task
    def randomCat_StatusCode(self):
        status_codes = [100, 101, 102, 103, 200, 201, 202, 203, 204, 206, 207, 300, 301, 302, 303, 304, 305, 307, 308, 400, 401, 402, 403, 404]
        random_url = "/" + str(random.choice(status_codes))
        res = self.client.get(random_url)
        print("Getting random Cat")

class MainTaskSet(HttpUser):
    host = "https://http.cat/"
    tasks = [TaskTest]
    wait_time = constant(1)
