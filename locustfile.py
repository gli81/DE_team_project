from locust import HttpUser, between, task

class WebsiteUser(HttpUser):
    wait_time = between(0.1, 0.2)

    @task
    def load_homepage(self):
        self.client.get("/")