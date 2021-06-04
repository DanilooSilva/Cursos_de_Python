import subprocess

proc = subprocess.run(
    ['ping', 'google.com'],
    capture_output=True,
    text=True
)

print(proc.stdout)