from locust import User, task, constant

class Demo1(User):
    weight = 2
    wait_time = constant(1)
    @task
    def openBrowser(self):
        print("Opening the first browser")

    @task
    def closeBrowser(self):
        print("Closing the first browser")

class Demo2(User):
    weight = 2
    wait_time = constant(1)
    @task
    def openBrowser(self):
        print("Opening the second browser")

    @task
    def closeBrowser(self):
        print("Closing the second browser")