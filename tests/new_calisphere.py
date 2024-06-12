

from words import words, letters, items
from random import choices, choice, randint

import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def home(self):
        self.client.get("/")

    @task(3)
    def search(self):
        for item_id in range(10):
            ws = "+".join(choices(words, k=randint(1,4)))
            print(ws)
            self.client.get(f"search/?q={ws}", name="/search")
            time.sleep(1)
    
    @task(2)
    def browse(self):
        self.client.get(f"collections/{choice(letters)}", name="/collection_browse")
    
    @task(5)
    def single_item(self):
        self.client.get(f"item/{choice(items)}", name="/item")

