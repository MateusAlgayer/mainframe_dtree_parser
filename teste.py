from typing import Generator


def value_generator() -> Generator:
    for i in range(10):
        yield i


def main():
    print("teste")

    for value in value_generator():
        print(value)


if __name__ == "__main__":
    main()
