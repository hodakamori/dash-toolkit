import datetime 

input_names = ("name", "age", "job")

def main(args):
    return " ".join([
        f'I am {args["name"]}.',
        f'I am {args["age"]} years old.',
        f'My job is {args["job"]}.',
        datetime.datetime.now().strftime('Date: %Y年%m月%d日 %H:%M:%S')
        ])
