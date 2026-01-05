import requests
import json
url = "https://api.themoviedb.org/3/movie/top_rated?language=en-US&page=1"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2MDJmNmI4NDQ0NmNiNTcxODY5ZWUyYzY1MjE3YzY1YiIsIm5iZiI6MTc2NzYzOTkxMy4wNDksInN1YiI6IjY5NWMwYjY5OTdiZDNmMTg3OTc2YTBkNyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.hVryin1glLdSqn54htVeO_IaUj9LVZmjTnj_L6TknIM"
}

response = requests.get(url, headers=headers)

data = response.json()

with open("top_rated.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

