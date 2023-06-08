from locust import User, task, constant


class MyTest(User):
    wait_time = constant(1)

    def on_start(self):
        print("On_Start is Starting")

    @task
    def task_1(self):
        print("Tasks Are Executing")

    def on_stop(self):
        print("On_Stop is Ending")