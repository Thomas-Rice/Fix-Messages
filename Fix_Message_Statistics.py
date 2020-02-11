import pandas as pd
import Fix_Message_Reader as Fmr
pd.set_option('display.max_columns', None)


def create_data_frame(data):
    data_frame = pd.DataFrame(data)
    data_frame['Side'] = pd.to_numeric(data_frame['Side'])
    data_frame['OrdType'] = pd.to_numeric(data_frame['OrdType'])
    data_frame['Quantity'] = pd.to_numeric(data_frame['Quantity'])
    data_frame['TimeInForce'] = pd.to_numeric(data_frame['TimeInForce'])
    data_frame['Price'] = pd.to_numeric(data_frame['Price'])
    return data_frame


def get_all_traded_products(data_frame):
    print(data_frame.Symbol.unique())


def get_most_popular_order(data_frame):
    print(data_frame['OrdType'].nlargest(1))


def get_stats_about_field(data_frame, field):
    print(data_frame[field].describe())


def group_by_average(data_frame, group_by, average):
    return data_frame.groupby([group_by])[average].mean()


def get_average_ordered_quantity_per_product(data_frame):
    print(group_by_average(data_frame, 'OrdType', 'Quantity'))


def get_average_price_per_product(data_frame):
    print(group_by_average(data_frame, 'OrdType', 'Price'))


if __name__ == "__main__":
    messages = Fmr.read_messages_file("./messages.txt")
    fix_messages = Fmr.format_lines_into_dict(messages)
    df = create_data_frame(fix_messages)

    # ** Statistics **
    print("List Of All Products Traded: ")
    get_all_traded_products(df)
    print("--- \n\n")

    print("Most Popular Order: ")
    get_most_popular_order(df)
    print("--- \n\n")

    print("Stats About OrdType: ")
    get_stats_about_field(df, 'OrdType')
    print("--- \n\n")

    print("Stats About Quantity: ")
    get_stats_about_field(df, 'Quantity')
    print("--- \n\n")

    print("Stats About Price: ")
    get_stats_about_field(df, 'Price')
    print("--- \n\n")

    print("Average Quantity per OrdType: ")
    get_average_ordered_quantity_per_product(df)
    print("--- \n\n")

    print("Average Price Per OrdType: ")
    get_average_price_per_product(df)