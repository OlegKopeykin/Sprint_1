time_str = '1h 45m,360s,25m,30m 120s,2h 60s'
total_minutes = 0

for value in time_str.split(','):
    for time in value.split(' '):
        if 's' in time:
            total_minutes += int(time.replace('s', '')) // 60

        if 'm' in time:
            total_minutes += int(time.replace('m', ''))

        if 'h' in time:
            total_minutes += int(time.replace('h', '')) * 60

print(total_minutes)