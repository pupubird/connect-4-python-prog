data = [
    [
        "X",
        "X",
        "X",
        "X",
        "X",
        "X"
    ], [
        "X",
        "X",
        "X",
        "X",
        "X",
        "X"
    ], [
        "X",
        "X",
        "X",
        "X",
        "X",
        "X"
    ]
]
for i in data:
    for j in i:
        if j == " ":
            print("yea")
            break
    else:
        continue
    break
else:
    print("draw")
