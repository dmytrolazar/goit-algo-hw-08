import heapq

def heap_sort(iterable, descending=False):
    sign = -1 if descending else 1
    h = [sign * el for el in iterable]
    heapq.heapify(h)
    return [sign * heapq.heappop(h) for _ in range(len(h))]

# 1. до найменшого кабеля приєднуємо з одного боку наступний по зростанню
# 2. з іншого боку приєднуємо третій
# 3. до передостаннього кабеля доєднуємо наступний
# 4. повторюємо крок 3 поки кабелі не закінчаться
def connect_cables(cables: list):
    # даний набір кабелів різної довжини
    print("Маємо набір кабелів різної довжини:", cables)
    # сортуємо масив за зростанням
    cables = heap_sort(cables)

    connection_order = []
    total_price = 0
    no_of_cables = len(cables)
    if no_of_cables < 2:
        print("Замало кабелів для з'єднання.")
    else:
        cable_prev_prev = cables.pop(0)
        cable_prev = cables.pop(0)
        connection_order.append((cable_prev_prev, cable_prev))
        total_price += cable_prev_prev + cable_prev
        if no_of_cables > 2:
            while len(cables) > 0:
                cable_this = cables.pop(0)
                connection_order.append((cable_this, cable_prev_prev))
                total_price += cable_prev_prev + cable_this
                cable_prev_prev = cable_prev
                cable_prev = cable_this
        print("Порядок з'єднання кабелів, парами:", connection_order)
        print("Загальні витрати на з'єднання кабелів:", total_price)

connect_cables([])
connect_cables([12])
connect_cables([12, 11])
connect_cables([12, 11, 13, 5, 6, 7])
