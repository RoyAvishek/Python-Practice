import requests

def check_service_availability(service_name, service_url):
    try:
        response = requests.get(service_url)
        if response.status_code == 200:
            print(f"{service_name} is up and running.")
        else:
            print(f"{service_name} is not available. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to {service_name}: {e}")

# Define the services and their URLs
services = {
    "Git": "https://github.com",
    "SonarQube": "http://sonarqube.example.com",
    "Nexus": "http://nexus.example.com",
    "Kubernetes": "https://kubernetes.example.com",
}

# Iterate over the services and check their availability
for service_name, service_url in services.items():
    check_service_availability(service_name, service_url)
