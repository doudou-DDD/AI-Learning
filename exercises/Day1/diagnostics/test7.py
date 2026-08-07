while True:
    try:
        value = int(input("请输入 1～10 之间的整数："))
    except ValueError:
        print("输入错误，请输入数字。")
        continue

    if value < 1 or value > 10:
        print("超出范围，请输入 1～10 之间的整数。")
        continue

    print("输入正确，程序结束。")
    break
