labirinto = [
    ["T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T"],
    ["T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "T", "T", "O", "O", "O", "T", "T", "T", "T", "T", "O", "T", "T"],
    ["T", "O", "T", "T", "T", "T", "O", "O", "O", "T", "O", "O", "O", "O", "O", "O", "O", "O", "O", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "O", "T", "T", "T", "T", "T", "O", "T", "T", "T", "T", "T", "T", "O", "T", "T", "O", "T", "O", "T", "T", "T", "T", "T", "O", "T", "T"],
    ["T", "O", "T", "T", "T", "T", "O", "T", "O", "T", "O", "T", "T", "O", "T", "T", "T", "T", "T", "T", "O", "O", "O", "T", "O", "O", "O", "T", "T", "T", "T", "T", "T", "T", "T", "T", "O", "T", "T", "T", "O", "O", "O", "T", "T", "T", "T", "T", "T", "O", "O", "O", "O", "T", "O", "O", "T", "T", "T", "O", "O", "O", "T"],
    ["T", "O", "T", "T", "T", "T", "O", "T", "O", "T", "O", "T", "T", "O", "T", "T", "T", "T", "T", "T", "O", "T", "O", "T", "O", "T", "O", "O", "O", "O", "T", "T", "T", "T", "T", "T", "O", "O", "O", "T", "O", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "O", "T", "T", "T", "O", "T", "T", "T", "O", "T", "T", "T"],
    ["T", "O", "T", "T", "T", "T", "O", "T", "O", "T", "O", "T", "T", "O", "O", "O", "O", "O", "T", "T", "O", "T", "O", "T", "O", "T", "T", "T", "T", "O", "O", "O", "O", "O", "O", "T", "T", "T", "O", "O", "O", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "O", "T", "T", "T", "O", "T", "T", "T"],
    ["T", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "T", "T", "T", "T", "O", "T", "T", "O", "T", "O", "T", "O", "T", "T", "T", "T", "O", "T", "T", "T", "T", "O", "O", "O", "T", "T", "O", "T", "T", "T", "T", "O", "T", "T", "T", "T", "T", "T", "O", "O", "O", "O", "O", "T", "T", "T", "O", "T", "T", "T"],
    ["T", "O", "T", "T", "T", "T", "T", "T", "T", "O", "T", "T", "O", "T", "T", "T", "O", "O", "T", "T", "O", "T", "O", "T", "O", "T", "T", "T", "T", "O", "T", "T", "T", "T", "T", "T", "O", "O", "T", "O", "T", "T", "T", "T", "O", "T", "T", "T", "T", "T", "T", "O", "T", "T", "T", "T", "T", "T", "T", "O", "T", "T", "T"],
    ["T", "O", "T", "T", "T", "T", "T", "T", "T", "O", "T", "T", "O", "T", "T", "T", "O", "T", "T", "T", "O", "T", "O", "T", "O", "O", "O", "O", "T", "O", "T", "T", "T", "T", "T", "T", "T", "T", "T", "O", "T", "T", "T", "T", "O", "T", "O", "O", "O", "T", "T", "O", "T", "T", "T", "T", "T", "T", "T", "O", "O", "O", "T"],
    ["T", "O", "T", "T", "T", "T", "T", "T", "T", "O", "T", "T", "O", "T", "T", "T", "O", "T", "O", "O", "O", "T", "O", "T", "O", "T", "T", "O", "T", "O", "O", "O", "O", "T", "T", "O", "T", "T", "T", "O", "O", "O", "O", "O", "O", "T", "O", "T", "O", "T", "T", "O", "T", "T", "T", "T", "T", "T", "T", "T", "T", "O", "T"],
    ["T", "O", "O", "O", "O", "O", "O", "O", "O", "O", "T", "T", "O", "T", "T", "T", "O", "T", "O", "T", "T", "T", "O", "T", "O", "T", "T", "O", "T", "T", "T", "T", "O", "T", "O", "O", "T", "T", "T", "T", "T", "O", "T", "T", "O", "T", "O", "T", "O", "O", "O", "O", "O", "O", "T", "T", "T", "T", "T", "T", "T", "O", "T"],
    ["T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "O", "T", "T", "T", "O", "T", "O", "O", "O", "O", "O", "T", "O", "T", "T", "O", "T", "T", "T", "T", "O", "T", "T", "O", "O", "O", "O", "T", "T", "O", "T", "T", "O", "O", "O", "T", "T", "T", "O", "T", "T", "O", "T", "T", "T", "T", "T", "T", "T", "O", "T"],
    ["T", "T", "T", "T", "T", "O", "O", "O", "T", "T", "T", "T", "O", "T", "T", "T", "O", "T", "O", "T", "T", "T", "T", "T", "O", "T", "T", "O", "O", "O", "O", "T", "O", "T", "T", "T", "T", "T", "O", "T", "T", "O", "T", "T", "O", "T", "O", "T", "T", "T", "O", "T", "T", "O", "O", "O", "O", "O", "O", "O", "O", "O", "T"],
    ["T", "T", "T", "T", "T", "O", "T", "O", "O", "T", "T", "T", "O", "T", "T", "T", "O", "T", "O", "T", "T", "T", "T", "T", "O", "T", "T", "T", "O", "T", "T", "T", "T", "T", "T", "T", "T", "T", "O", "T", "T", "T", "O", "O", "O", "T", "T", "T", "T", "T", "O", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T"],
    ["T", "T", "T", "T", "T", "O", "T", "T", "O", "T", "T", "T", "O", "T", "T", "T", "O", "T", "O", "T", "T", "O", "O", "O", "O", "O", "O", "T", "O", "T", "T", "T", "T", "T", "O", "O", "O", "O", "O", "T", "T", "T", "O", "T", "O", "T", "T", "T", "T", "T", "O", "O", "O", "T", "T", "T", "O", "T", "T", "O", "T", "T", "T"],
    ["T", "T", "T", "O", "O", "O", "T", "T", "O", "T", "T", "T", "O", "T", "T", "T", "O", "O", "O", "O", "T", "O", "T", "T", "T", "T", "O", "T", "O", "T", "T", "T", "T", "T", "O", "T", "T", "T", "T", "T", "T", "T", "O", "O", "O", "T", "O", "T", "T", "T", "T", "T", "O", "T", "T", "T", "O", "T", "T", "O", "T", "T", "T"],
    ["T", "T", "T", "O", "T", "T", "T", "O", "O", "T", "T", "T", "O", "T", "T", "T", "O", "T", "T", "T", "T", "O", "T", "T", "T", "T", "O", "T", "T", "T", "T", "O", "T", "T", "O", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "O", "O", "T", "T", "T", "T", "O", "T", "T", "O", "O", "O", "O", "O", "T", "T", "T"],
    ["T", "T", "T", "O", "T", "T", "T", "O", "T", "T", "T", "T", "O", "T", "T", "T", "O", "T", "T", "T", "T", "O", "T", "T", "T", "T", "O", "O", "O", "O", "T", "O", "T", "T", "O", "T", "T", "O", "O", "O", "O", "O", "T", "T", "T", "T", "T", "O", "T", "T", "T", "T", "O", "T", "O", "O", "T", "O", "T", "O", "T", "T", "T"],
    ["T", "T", "T", "O", "T", "O", "T", "O", "T", "T", "T", "T", "O", "T", "T", "T", "O", "T", "T", "T", "T", "O", "T", "T", "T", "T", "O", "T", "T", "O", "T", "O", "T", "T", "O", "T", "T", "O", "T", "T", "T", "O", "T", "T", "O", "O", "O", "O", "T", "T", "O", "O", "O", "O", "O", "T", "T", "O", "T", "O", "O", "O", "T"],
    ["T", "T", "T", "O", "T", "O", "O", "O", "O", "O", "O", "O", "O", "T", "T", "T", "O", "O", "O", "O", "T", "O", "T", "T", "T", "T", "O", "T", "T", "O", "O", "O", "O", "O", "O", "O", "T", "O", "T", "T", "T", "O", "T", "T", "O", "T", "T", "O", "T", "T", "O", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "O", "T"],
    ["T", "T", "T", "O", "T", "T", "O", "T", "T", "T", "T", "T", "T", "T", "O", "O", "O", "T", "T", "O", "T", "O", "T", "T", "T", "T", "O", "T", "T", "T", "T", "T", "T", "T", "T", "O", "O", "O", "T", "T", "T", "O", "T", "T", "O", "T", "T", "O", "T", "T", "O", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "O", "T"],
    ["T", "T", "T", "O", "T", "T", "O", "T", "T", "T", "T", "T", "T", "T", "O", "T", "T", "T", "T", "O", "O", "O", "T", "T", "O", "O", "O", "T", "T", "T", "T", "T", "T", "T", "T", "O", "T", "O", "O", "O", "O", "O", "O", "O", "O", "T", "T", "O", "T", "T", "O", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "O", "T"],
    ["T", "T", "T", "O", "T", "O", "O", "O", "T", "T", "T", "O", "O", "O", "O", "T", "T", "T", "T", "T", "O", "T", "T", "T", "O", "T", "T", "T", "O", "O", "O", "O", "O", "T", "T", "O", "T", "T", "T", "T", "O", "T", "T", "T", "T", "T", "T", "O", "T", "T", "O", "T", "T", "O", "O", "O", "T", "T", "T", "T", "T", "O", "T"],
    ["T", "T", "T", "O", "T", "O", "T", "O", "O", "T", "T", "O", "T", "T", "T", "T", "T", "T", "T", "T", "O", "T", "O", "T", "O", "T", "T", "T", "T", "T", "T", "T", "O", "T", "T", "O", "T", "T", "T", "T", "O", "T", "T", "T", "T", "T", "T", "O", "T", "T", "O", "T", "T", "O", "T", "O", "O", "O", "O", "O", "O", "O", "T"],
    ["T", "T", "T", "O", "T", "T", "T", "T", "O", "T", "T", "O", "O", "T", "T", "O", "O", "O", "O", "O", "O", "T", "O", "T", "O", "O", "O", "O", "T", "T", "T", "T", "O", "T", "O", "O", "O", "O", "O", "O", "O", "T", "T", "O", "O", "O", "O", "O", "T", "T", "O", "O", "O", "O", "T", "T", "T", "T", "T", "T", "T", "T", "T"],
    ["T", "T", "T", "O", "T", "O", "O", "T", "T", "T", "T", "T", "O", "T", "T", "O", "T", "T", "T", "T", "O", "T", "O", "T", "T", "T", "T", "O", "T", "T", "T", "O", "O", "O", "O", "T", "O", "T", "T", "T", "T", "T", "T", "O", "T", "T", "T", "T", "T", "T", "O", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T"],
    ["T", "T", "T", "O", "T", "T", "O", "T", "O", "T", "O", "T", "O", "T", "T", "O", "T", "T", "T", "T", "O", "T", "O", "O", "T", "T", "T", "O", "T", "T", "T", "O", "T", "T", "O", "O", "O", "T", "T", "O", "T", "T", "T", "O", "T", "T", "T", "T", "O", "T", "O", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "O", "T"],
    ["T", "T", "T", "O", "T", "T", "O", "T", "O", "T", "O", "T", "O", "T", "T", "O", "T", "T", "T", "T", "O", "T", "T", "O", "T", "T", "T", "O", "O", "O", "O", "O", "T", "T", "T", "T", "T", "T", "T", "O", "T", "T", "T", "O", "T", "T", "O", "O", "O", "T", "O", "T", "T", "T", "T", "T", "O", "O", "O", "O", "O", "O", "T"],
    ["T", "T", "T", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "T", "T", "T", "T", "O", "O", "T", "O", "O", "O", "O", "O", "T", "T", "T", "O", "T", "T", "T", "T", "T", "T", "T", "O", "T", "T", "T", "O", "T", "O", "O", "T", "T", "T", "O", "T", "T", "T", "T", "T", "O", "T", "T", "T", "T", "O", "T"],
    ["T", "T", "T", "T", "O", "T", "T", "O", "T", "T", "O", "T", "T", "T", "O", "T", "T", "T", "T", "T", "T", "O", "T", "O", "T", "O", "T", "T", "T", "O", "T", "O", "T", "T", "T", "O", "T", "O", "O", "O", "T", "T", "T", "O", "T", "T", "O", "O", "O", "T", "O", "O", "O", "O", "O", "O", "O", "T", "T", "T", "T", "O", "T"],
    ["T", "T", "T", "T", "O", "T", "T", "O", "T", "T", "O", "T", "T", "T", "O", "T", "T", "T", "O", "O", "O", "O", "T", "O", "T", "O", "T", "T", "T", "O", "T", "O", "T", "T", "T", "O", "T", "T", "T", "O", "T", "T", "T", "O", "T", "T", "T", "T", "O", "T", "T", "T", "T", "O", "T", "T", "T", "T", "T", "T", "T", "O", "T"],
    ["T", "T", "T", "T", "O", "T", "T", "O", "T", "T", "O", "T", "O", "T", "O", "T", "T", "T", "O", "T", "T", "T", "O", "O", "T", "O", "T", "O", "O", "O", "O", "O", "O", "O", "O", "O", "T", "T", "T", "O", "T", "O", "T", "O", "T", "T", "T", "T", "O", "O", "T", "T", "T", "O", "T", "T", "T", "T", "T", "T", "T", "O", "T"],
    ["T", "T", "O", "T", "O", "O", "T", "O", "T", "T", "O", "T", "O", "T", "O", "T", "T", "T", "O", "T", "T", "T", "O", "T", "T", "O", "T", "O", "T", "T", "O", "T", "T", "O", "T", "T", "T", "T", "T", "O", "T", "O", "T", "O", "T", "T", "T", "T", "T", "O", "O", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "O", "T"],
    ["T", "T", "O", "T", "T", "O", "T", "O", "T", "T", "O", "T", "O", "T", "O", "T", "T", "T", "O", "O", "T", "T", "O", "T", "O", "O", "T", "O", "T", "T", "O", "T", "T", "T", "T", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "T", "T", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "T"],
    ["T", "T", "O", "O", "T", "O", "T", "O", "O", "O", "O", "T", "O", "T", "O", "O", "O", "O", "O", "O", "O", "O", "O", "T", "O", "T", "T", "T", "O", "O", "O", "T", "T", "O", "T", "T", "O", "T", "T", "O", "T", "T", "T", "T", "T", "O", "T", "O", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T"],
    ["T", "T", "T", "O", "T", "O", "T", "T", "T", "T", "T", "T", "O", "T", "T", "T", "T", "T", "T", "O", "T", "T", "T", "T", "O", "T", "T", "O", "T", "T", "T", "T", "T", "O", "T", "T", "O", "T", "T", "O", "T", "T", "T", "T", "T", "O", "T", "O", "O", "T", "T", "O", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T"],
    ["T", "T", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "T", "T", "O", "O", "O", "O", "O", "T", "T", "T", "T", "T", "T", "T", "O", "T", "T", "O", "T", "T", "O", "T", "T", "O", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "O", "O", "O", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T"],
    ["T", "T", "O", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "O", "T", "T", "T", "T", "T", "O", "T", "T", "O", "T", "T", "O", "T", "T", "T", "T", "T", "T", "T", "T", "T", "O", "O", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T"],
    ["T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "O", "T", "T", "O", "T", "T", "O", "T", "T", "O", "T", "T", "O", "T", "T", "T", "T", "T", "T", "T", "T", "T", "O", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T"],
    ["T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "O", "T", "T", "O", "T", "T", "X", "T", "T", "T", "T", "T", "T", "T", "T", "T", "O", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T"]
]

