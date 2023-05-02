import threading
# Функція для пошуку моди у підмасиві
def find_mode(arr):
    mode = None
    max_count = 0
    counts = {}
    for x in arr:
        if x not in counts:
            counts[x] = 1
        else:
            counts[x] += 1
        if counts[x] > max_count:
            mode = x
            max_count = counts[x]
    return mode
# Функція для обчислення моди варіаційного ряду
def find_variation_mode(variation):
    modes = []
    num_threads = len(variation)
    threads = []
    for i in range(num_threads):
        t = threading.Thread(target=lambda mode_list, arr: mode_list.append(find_mode(arr)), args=(modes, variation[i]))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    return find_mode(modes)
variation = [[1, 2, 2, 3, 4], [2, 2, 2, 3, 5], [1, 1, 2, 2, 3]]
mode = find_variation_mode(variation)
print(mode)