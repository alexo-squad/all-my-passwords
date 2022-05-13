import random
import string

def random_num(loop_count=1):
    ret = []
    # Add a random number between 0 - 255 to the password
    for loop in range(loop_count):
        ret.append(str(random.randrange(0, 500)))
    return ret

def random_str(loop_count=1):
    ret = []
    # Add a random char to the password
    for loop in range(loop_count):
        ret.append(random.choice(string.ascii_letters))
    return ret

# start every password with "pass". It makes it secure
random_pass: list = ["myPass-"]

random_pass.extend(random_num(loop_count=5))
random_pass.extend(random_str(loop_count=10))
print("".join(random_pass).strip())
