num = int(input("请输入购买商品件数： "))
sum_0 = int(input("请输入商品总金额： "))


def sale(sum_1):
    end_sum = sum_1
    end_sum = format(end_sum, '.2f')
    dis_sum = sum_0 * 0.1
    dis_sum = format(dis_sum, '.2f')
    return f"可得到折扣额={dis_sum}""\n"f"折扣后应付金额={end_sum}"


if 2 <= num < 5:
    sum_2 = sum_0*0.9
    print(sale(sum_2))

elif num >= 5 and sum_0 >= 1000:
    sum_2 = sum_0*0.85
    print(sale(sum_2))

else:
    sum_2 = sum_0 * 0.9
    print(sale(sum_2))
