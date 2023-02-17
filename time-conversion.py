# Read an integer value, which is the duration in seconds of a certain event in a factory, and inform it expressed in hours:minutes:seconds.

seconds = int(input())

hours = seconds // 3600
minutes = seconds // 60
seconds = seconds % 60

print(f'{hours}:{minutes}:{seconds}')