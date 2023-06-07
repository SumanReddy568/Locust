from locust import HttpUser, task, constant

class testGetuser(HttpUser):
    host = "https://reqres.in"
    @task
    def testget(self):
        wait_time = constant(1)
        res=self.client.get("/api/users?page=2")
        print(res.status_code)
        print(res.text)
        print(res.headers)

    @task
    def testPost(self):
        wait_time=constant(1)
        res=self.client.post("/api/users",data={
    "name": "Chinadurai",
    "job": "devops",
    "id": "420",
    "createdAt": "2023-06-06T11:44:42.629Z"})
        print(res.status_code)
        print(res.text)
        print(res.headers)

