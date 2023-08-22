def foo(n: int) -> None:
    print(f"{n=}")
    # breakpoint()
    if n < 10:
        print("< 10")
    else:
        print("> 10")


foo(12)
