import time
print("Waiting for the instances to spin up.", end="", flush=True)
for i in range(10):
    time.sleep(1)
    print(".", end="", flush=True)
print()
