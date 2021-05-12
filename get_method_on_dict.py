user_id_to_name = {
    152623: "Adam",
    456235: "Brian",
    763563: "Jeffrey",
}

def say_hello(user_id: int):
    return "Hello {}".format(user_id_to_name.get(user_id, "there"))

print(say_hello(456235))

print(say_hello(234639))