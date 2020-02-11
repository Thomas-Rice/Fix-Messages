def read_messages_file(file_path):
    file = open(file_path, 'r')
    return file.readlines()


def get_field_value(field, message):
    results = message.split("|")
    field_search_value = f"{field}="
    for result in results:
        if field_search_value in result:
            value = result.split(field_search_value)[1]
            return value


def create_dictionary():
    return {"MsgType": [],
            "Symbol": [],
            "Side": [],
            "Quantity": [],
            "OrdType": [],
            "TimeInForce": [],
            "SecurityType": [],
            "Account": [],
            "Price": []}


def format_lines_into_dict(lines):
    fix_messages = create_dictionary()
    for line in lines:
        field_and_value = line.strip()
        fix_messages["MsgType"].append(get_field_value("35", field_and_value))
        fix_messages["Symbol"].append(get_field_value("55", field_and_value))
        fix_messages["Side"].append(get_field_value("54", field_and_value))
        fix_messages["Quantity"].append(get_field_value("38", field_and_value))
        fix_messages["OrdType"].append(get_field_value("40", field_and_value))
        fix_messages["TimeInForce"].append(get_field_value("59", field_and_value))
        fix_messages["SecurityType"].append(get_field_value("167", field_and_value))
        fix_messages["Account"].append(get_field_value("1", field_and_value))
        fix_messages["Price"].append(get_field_value("44", field_and_value))
    return fix_messages

