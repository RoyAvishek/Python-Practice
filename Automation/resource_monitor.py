# System Resource Monitor: Develop a script that collects and displays system resource usage information (e.g., CPU, memory, disk) in real-time.

import psutil

def monitor_resources():
    while True:
        cpu_percent = psutil.cpu_percent(interval=1)
        mem_usage = psutil.virtual_memory().percent

        print(f"CPU Usage: {cpu_percent}%")
        print(f"Memory Usage: {mem_usage}%")
        print("-------------------------")

if __name__ == "__main__":
    monitor_resources()
