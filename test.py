#тест кода
#timer
import time

# старт таймера
begin_time = time.time()

# выполняем продолжительное действие
time.sleep(1)

# получаем время окончания действия с начала запуска таймера
end_time = time.time()
print end_time - begin_time

# другое продолжительное действие
time.sleep(2)

# получаем время окончания действия с начала запуска таймера
end_time = time.time()
print end_time - begin_time

"""
#перевод секунд в минуты и часы
m, s = divmod(seconds, 60)
h, m = divmod(m, 60)
print "%d:%02d:%02d" % (h, m, s)
"""
