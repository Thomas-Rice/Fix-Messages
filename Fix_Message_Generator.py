from random import randint

randomNumberMaxRange = 1000


def generate_message(symbol, side, quantity, ordType, timeInForce, securityType, account, price):
    return f"8=FIX.4.2|35=D|55={symbol}|54={side}|38={quantity}|40={ordType}|59={timeInForce}|167={securityType}|1={account}|44={price}"


def generate_symbol():
    return f"SYMBOL_{randint(0, randomNumberMaxRange)}"


def generate_side():
    return randint(1, 2)


def generate_quantity():
    return randint(0, randomNumberMaxRange)


def generate_ordtype():
    return randint(1, 5)


def generate_timeInForce():
    return randint(0, 6)


def generate_securitytype():
    types = ["FUT", "OPT", "CS"]
    index_to_choose = randint(0, len(types) - 1)
    return types[index_to_choose]


def generate_account():
    return f"CLIENT_{randint(0, randomNumberMaxRange)}"


def generate_price():
    return f"{randint(0, randomNumberMaxRange)}.{randint(0, 99)}"


def generate_fix_messages(number_of_messages_to_generate):
    fake_messages = []
    for i in range(number_of_messages_to_generate):
        fake_message = generate_message(generate_symbol(), generate_side(), generate_quantity(), generate_ordtype(),
                                      generate_timeInForce(), generate_securitytype(), generate_account(), generate_price())
        print(fake_message)
        fake_messages.append(fake_message)
    WriteToFile(fake_messages)


def WriteToFile(messages):
    f = open("./messages.txt", "w")
    for message in messages:
        f.write(message + "\n")
    f.close()


if __name__ == "__main__":
    generate_fix_messages(1000)
