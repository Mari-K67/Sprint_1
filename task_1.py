time_line = '1h 45m,360s,25m,30m 120s,2h 60s'
time_line = time_line.replace(' ', ',')
time_list = time_line.split(',')
counter = 0

for i in time_list:
    if 'h' in i:
        i = int(i[:-1])
        counter += i*60
    elif 's' in i:
        i = int(i[:-1])
        counter += i/60
    else:
        i = int(i[:-1])
        counter += i 


counter = int(counter)

print(counter)