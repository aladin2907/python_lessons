names: list[str] = ["John", "Marry"]

_names = iter(names)
print(next(_names))
print(next(_names))
print(next(_names))
while True:
    try:
        value = next(_names)
        print(f"{value=}")
    except StopIteration:
        break
