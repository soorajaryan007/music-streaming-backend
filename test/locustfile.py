from locust import HttpUser, task, between

class SongUser(HttpUser):

    wait_time = between(0.1, 0.5)

    @task
    def get_songs(self):
        self.client.get("/songs")