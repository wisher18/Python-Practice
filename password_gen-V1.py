import random
import string

pass_db = [list(string.ascii_uppercase), list(string.ascii_lowercase), list(string.punctuation), list(string.digits)]
pass_len = int(input("LENGTH (Minimum 14 Recommended.)   >>>   "))


def gen_pass():
    pass_gen = ""
    for i in range(pass_len):
        pass_gen += str(random.choice(random.choice(pass_db)))
    replacements = (('s', '$'), ('i', '!'), ('a', '@'), ('e', '3'), ('l', '1'), ('s', '5'), ('t', '+'))
    my_string = pass_gen
    new_string = my_string
    for old, new in replacements:
        new_string = new_string.replace(old, new)
    return new_string


def db_update(final_pass):
    with open("mypass.txt", "a+") as DB:
        discard_pass_gen = ("Duplicate Error." for lines in DB if final_pass in lines)
        if discard_pass_gen != "Duplicate Error.":
            DB.write(f"\n{final_pass}")
    return discard_pass_gen


pass_loop = int(input("How Many Passwords Should Be Generated?   >>>   "))
for i in range(pass_loop):
    final_pass = gen_pass()
    discard = db_update(final_pass)
    if discard == "Duplicate Error.":
        i -= 1
        continue
    print(f"\n\n\t\t\t{i+1}. {final_pass}")
