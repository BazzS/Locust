from locust import HttpUser, task, TaskSet

class TestUser(TaskSet):

    @task(1)
    def hello_world(self):
        self.client.get("http://localhost:8000")

class WebsiteUser(HttpUser):
    tasks = [TestUser]
