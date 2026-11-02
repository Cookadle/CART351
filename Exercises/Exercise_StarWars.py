import requests
from rich import print

response = requests.get("https://swapi.dev/api/planets/")
data = response.json()

planets = data["results"]

for planet in planets:
    print(f"[bold cyan]{planet['name']}[/bold cyan]")
    print(f"  Diameter: [yellow]{planet['diameter']}[/yellow]")
    print(f"  Population: [green]{planet['population']}[/green]")
