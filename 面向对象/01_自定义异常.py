class ShortInputException(Exception):
    def __init__(self, length, atleast):
        # super().__init__()
        self.length = length
        self.atleast = atleast


def main():
    s = input("请输入---")
    if len(s) < 3:
        raise ShortInputException(len(s), 3)


if __name__ == '__main__':
    try:
        main()
    except ShortInputException as result:
        print(result.length)
