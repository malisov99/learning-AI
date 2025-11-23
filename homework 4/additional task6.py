#Задача 6. Возможный размен

"""Напишите программу, которая будет определять, можно ли составить конкретную сумму из определенного количества монет. 
Например, можно набрать доллар из четырех монет номиналом в 25 центов. Но при помощи пяти монет доллар никак не собрать. 
При этом из шести монет это снова возможно, если взять три монеты по 25 центов, две – по 10 и одну номиналом в 5 центов. 
Также возможно собрать сумму $1,25 из пяти, семи или восьми монет, но не удастся это сделать с четырьмя или шестью монетами. 
Ваша основная программа должна запрашивать у пользователя искомую сумму и количество монет. 
На выходе вы должны получить сообщение о том, можно или нет собрать введенную сумму при помощи заданного количества монет. 
Представьте, что для решения этой задачи в вашем распоряжении есть монеты номиналом 1, 5, 10 и 25 центов. 
Также ваша программа должна включать рекурсивный алгоритм. Циклов в ней быть не должно."""

def can_form_amount(amount, coins_count, coin_types):

    if amount == 0 and coins_count == 0:
        return True

    if amount < 0 or coins_count == 0:
        return False

    if not coin_types:
        return False

    current_coin = coin_types[0]

    with_coin = can_form_amount(amount - current_coin, coins_count - 1, coin_types)

    without_coin = can_form_amount(amount, coins_count, coin_types[1:])

    return with_coin or without_coin

if __name__ == "__main__":
    target_sum = float(input("Введите сумму (в долларах): "))
    total_coins = int(input("Введите количество монет: "))

    cents_needed = int(round(target_sum * 100))
    denominations = [25, 10, 5, 1]

    if can_form_amount(cents_needed, total_coins, denominations):
        print(f"Можно собрать ${target_sum:.2f} из {total_coins} монет.")
    else:
        print(f"Невозможно собрать ${target_sum:.2f} из {total_coins} монет.")