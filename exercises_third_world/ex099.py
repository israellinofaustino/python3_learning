from time import sleep

num_list = ()

def line():
    print("-=" * 25)


def max_num(*num):
    num_list = num

    print("Analyzing informed values...")
    sleep(2.5)
    for n in num_list:
        print(n, end=" ", flush=True)
        sleep(0.5)

    if len(num_list) >= 1:
        print(f" => A total of {len(num_list)} value(s) was reported!", end="")
        print()
        print(f"The highest reported value was {max(num_list)}.")
    elif len(num_list) < 1:
        print("No value was reported!")
        print("There is no greater value to display.")


line()
max_num(2, 9, 4, 5, 7, 1)
line()
max_num(4, 7, 0)
line()
max_num(1, 2)
line()
max_num(6)
line()
max_num(0)
line()
max_num(0, 0, 0)
line()
max_num()
line()
