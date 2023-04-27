from time import sleep


def line():
    print("-=" * 20)


def counter(start, end, step):
    if step == 0:
        step = 1
    print(f"Count from {start} to {end} of {step} in {step}")
    sleep(2.5)
    count = start
    if start < end:
        while count <= end:
            print(count, end=" ", flush=True)
            sleep(0.5)
            count += step
        print("END", end="")
        print()
    else:
        count = start
        while count >= end:
            print(count, end=" ", flush=True)
            sleep(0.5)
            count -= step
        print("END", end="")
        print()
line()
counter(1, 10, 1)
line()
counter(10, 0, 2)
line()

print("Now it's your turn to customize the count.")
start = int(input("Start from: "))
end = int(input("End: "))
step = abs(int(input("Steps: ")))

counter(start, end, step)
line()