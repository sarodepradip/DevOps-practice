import psutil
import time 
import logging
import smtplib
from email.mime.text import MIMEText

# configuration

CPU_THRESHOLD = 50

MEMORY_THRESHOLD = 70
DISK_THRESHOLD = 80

CHECK_INTERVAL = 5 # seconds

# Email config (optional)
EMAIL_SENDER = "sarodepradip366@gmail.com"
EMAIL_PASSWORD = "pradip1234"
EMAIL_RECEIVER = "receiver@gmail.com"

# Logging setup

logging.basicConfig(
    filename="system_monitor.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s" 
)

# Function 

def get_system_stats():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('C:\\').percent
    return cpu, memory, disk  

def log_status(cpu,memory, disk):
    message = f"CPU: {cpu}% | memory: {memory}% | Disk: {disk}%"
    print(message)
    logging.info(message)
    
def send_email_alert(message):
    try:
        msg = MIMEText(message)
        msg['Subject'] = "system Alert"
        msg['from'] = EMAIL_SENDER
        msg['To'] = EMAIL_RECEIVER
        
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
        
        print("Email alert sent!")
        
    except Exception as e:
        print("Email failed:",e)
        
def check_thresholds(cpu, memory, disk):
    alert_message = ""
    
    if cpu > CPU_THRESHOLD:
        alert_message += f"High CPU: {cpu}%\n"
        
    if memory > MEMORY_THRESHOLD:
        alert_message += f"High Memory: {memory}%\n"
        
    if disk > DISK_THRESHOLD:
        alert_message += f"High Disk: {disk}%\n"
    
    return alert_message

# main program

def main():
    print("starting system monitor...\n")
    
    while True:
        cpu, memory, disk = get_system_stats()
        log_status(cpu, memory, disk)
        
        alert = check_thresholds(cpu, memory, disk)
        
        if alert:
            print("ALERT DETECTED!")
            print(alert)
            
            # send email (optional)
            
        time.sleep(CHECK_INTERVAL)
            # correct placement
if __name__=="__main__":
    main()
    
    
    