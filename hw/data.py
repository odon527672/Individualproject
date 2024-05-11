import time
import psutil
import os

def initialize_bars(cpu_usage, mem_usage, disk_usage, bars=50):
    cpu_percent = cpu_usage / 100
    cpu_bar = '█' * int(cpu_percent * bars) + '-' * (bars - int(cpu_percent * bars))
    cpu_bar = f"{cpu_bar: <{bars}}"

    mem_percent = mem_usage / 100
    mem_bar = '█' * int(mem_percent * bars) + '-' * (bars - int(mem_percent * bars))
    mem_bar = f"{mem_bar: <{bars}}"

    disk_percent = disk_usage / 100
    disk_bar = '█' * int(disk_percent * bars) + '-' * (bars - int(disk_percent * bars))
    disk_bar = f"{disk_bar: <{bars}}"

    return cpu_bar, mem_bar, disk_bar

def display_usage(cpu_bar, mem_bar, disk_bar, cpu_usage, mem_usage, disk_usage):
    print(f"CPU Usage: |{cpu_bar}| {cpu_usage:.2f}%")
    print(f"MEM Usage: |{mem_bar}| {mem_usage:.2f}%")
    print(f"Disk Usage: |{disk_bar}| {disk_usage:.2f}%")

cpu_bar, mem_bar, disk_bar = initialize_bars(psutil.cpu_percent(), psutil.virtual_memory().percent, psutil.disk_usage('/').percent)

while True:
    cpu_usage = psutil.cpu_percent()
    mem_usage = psutil.virtual_memory().percent
    disk_percent = psutil.disk_usage('/').percent
    display_usage(cpu_bar, mem_bar, disk_bar, cpu_usage, mem_usage, disk_percent)
    time.sleep(0.5)