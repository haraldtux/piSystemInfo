#!/usr/bin/python
#
# ^H> HucDuino 02-12-2018
#
## Raspberry Pi Python Cli piSystemInfo
#

from datetime import datetime
import psutil
import vcgencmd
import subprocess
import os

color1 = '\033[1;34;40m' # blue
color2 = '\033[1;31;40m' # red
color3 = '\033[1;32;40m' # green
color4 = '\033[0;37;40m' # white

def clean_screen():
    if psutil.POSIX:
        os.system('clear')
    else:
        os.system('cls')

def cpu_generic_details():
    items = [s.split('\t: ') for s in subprocess.check_output(["cat /proc/cpuinfo  | grep 'model name\|Hardware\|Serial' | uniq "], shell=True).splitlines()]
    return items

def memory():
    memory = psutil.virtual_memory()
    # Divide from Bytes -> KB -> MB
    available = round(memory.available/1024.0/1024.0,1)
    total = round(memory.total/1024.0/1024.0,1)
    return str(total) + 'MB total / ' + str(available) + 'MB free ( ' + str(memory.percent) + '% )'

def disk():
    disk = psutil.disk_usage('/')
    # Divide from Bytes -> KB -> MB -> GB
    free = round(disk.free/1024.0/1024.0/1024.0,1)
    total = round(disk.total/1024.0/1024.0/1024.0,1)
    return str(total) + 'GB total / ' + str(free) + 'GB free ( ' + str(disk.percent) + '% )'    
    
cpu_genric_info = cpu_generic_details()
pi_model = subprocess.check_output("cat /proc/device-tree/model | cut -d= -f2", shell=True).replace('\n', '')
cpuTemp = subprocess.check_output("vcgencmd measure_temp| cut -d= -f2", shell=True).replace('\n', '')
CPUp = str(psutil.cpu_percent(interval=1))
core_frequency = subprocess.check_output("vcgencmd get_config arm_freq | cut -d= -f2", shell=True).replace('\n', '')
proc_info = subprocess.check_output("nproc", shell=True).replace('\n', '')
core_volt = subprocess.check_output("vcgencmd measure_volts| cut -d= -f2", shell=True).replace('\n', '')
uptime = subprocess.check_output("uptime -p |awk -F, '{print $1,$2,$3}'", shell=True).replace('\n', '')
started = subprocess.check_output("uptime -s", shell=True).replace('\n', '')
sys_time = datetime.now().strftime("%d %b %Y , %H : %M : %S")

clean_screen()
print ' '
print (color1 + '^H> HucDuino')
print ' '
print (color1 + 'Raspberry Pi Hardware :')
print (color2 + 'Model           : ' + color3 + pi_model)
print (color2 + 'Hardware Type   : ' + color3 + cpu_genric_info[1][1])
print (color2 + 'Serial Number   : ' + color3 + cpu_genric_info[2][1])
print (color2 + 'Processor Type  : ' + color3 + cpu_genric_info[0][1])
print (color2 + 'Core Frequency  : ' + color3 + core_frequency + 'Mhz')
print (color2 + 'No of Cores     : ' + color3 + proc_info) 
print (color2 + 'CPU Temperature : ' + color3 + cpuTemp)
print (color2 + 'Core Volt       : ' + color3 + core_volt)
print (color2 + 'CPU Usage       : ' + color3 + CPUp + '%')
print (color1 + 'System :')
print (color2 + 'System Time     : ' + color3 + sys_time)
print (color2 + 'Uptime          : ' + color3 + uptime)
print (color2 + 'Started on      : ' + color3 + started)
print (color2 + 'Memory          : ' + color3 + memory())
print (color2 + 'Disk            : ' + color3 + disk() + color4)
print ' '
