import psutil

def check_cpu():
    threshold = int(input("Enter CPU threshold (%): "))
    
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"Current CPU Usage: {cpu_usage}%")
    
    if cpu_usage > threshold:
        print("ALERT: CPU usage Usage is high!")
    else:
        print("CPU Usage is normal")
check_cpu() 
