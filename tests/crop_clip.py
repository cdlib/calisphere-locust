from words import thumbs
from random import choice

from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 4)

    @task(4)
    def clip(self):
        path = f"/clip/500x500/{choice(thumbs)}"
        print(path)
        self.client.get(path, name="/clip500")
    
    @task(2)
    def crop120(self):
        path = f"/crop/120x120/{choice(thumbs)}"
        print(path)
        self.client.get(path, name="/crop120")
    
    @task(2)
    def crop210(self):
        path = f"/crop/210x210/{choice(thumbs)}"
        print(path)
        self.client.get(path, name="/crop210")