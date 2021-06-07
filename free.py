#!/usr/bin/python3

import subprocess
import re

ps = subprocess.Popen(['ps', '-caxm', '-orss,comm'], stdout=subprocess.PIPE).communicate()[0].decode()
vm = subprocess.Popen(['vm_stat'], stdout=subprocess.PIPE).communicate()[0].decode()

def print_stat(vm_stats, msg_tpl, entry_key, unit):
    if unit.upper() == "GB":
        stat = vm_stats[entry_key]/1024/1024/1024
    else:
        stat = vm_stats[entry_key]/1024/1024
    print(msg_tpl % ( stat ))

def print_stat_integer(vm_stats, entry_name, entry_key, unit):
    msg_tpl = "{}:\t\t%d {}".format(entry_name, unit.upper())
    print_stat(vm_stats, msg_tpl, entry_key, unit)

def print_stat_float(vm_stats, entry_name, entry_key, unit):
    msg_tpl = "{}:\t\t%.3f {}".format(entry_name, unit.upper())
    print_stat(vm_stats, msg_tpl, entry_key, unit)  

process_lines = ps.split('\n')
sep = re.compile('[\s]+')
rss_total = 0
for row in range(1,len(process_lines)):
    row_text = process_lines[row].strip()
    row_elem = sep.split(row_text)
    try:
        rss = float(row_elem[0]) * 1024
    except:
        rss = 0
    rss_total += rss

vm_lines = vm.split('\n')
sep = re.compile(':[\s]+')
vm_stats = {}
for row in range(1,len(vm_lines)-2):
    row_text = vm_lines[row].strip()
    row_elem = sep.split(row_text)
    vm_stats[(row_elem[0])] = int(row_elem[1].strip('\.')) * 4096

vm_stats['Real Mem Total'] = rss_total
print_stat_integer(vm_stats, 'Wired Mem', 'Pages wired down', 'MB')
print_stat_integer(vm_stats, 'Active Mem', 'Pages active', 'MB')
print_stat_integer(vm_stats, 'Inactive Mem', 'Pages inactive', 'MB')
print_stat_integer(vm_stats, 'Free Mem', 'Pages free', 'MB')
print_stat_float(vm_stats, 'Real Mem Total', 'Real Mem Total', 'GB')
