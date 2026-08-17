from machine import Pin
import time
import ugit

# Настройка кнопки BOOT (GPIO 0 на большинстве плат ESP32) с подтяжкой к питанию
button = Pin(0, Pin.IN, Pin.PULL_UP)

print("Нажмите кнопку BOOT для синхронизации с GitHub через ugit...")

while True:
    # Кнопка при нажатии замыкается на GND (уровень LOW)
    if button.value() == 0:
        print("Кнопка нажата! Запуск синхронизации...")
        try:
            # Вызов функции обновления репозитория
            ugit.pull_all()
            print("Синхронизация успешно завершена!")
        except Exception as e:
            print("Ошибка обновления:", e)
        
        # Антидребезг и задержка от повторного срабатывания
        time.sleep(2)
        
    time.sleep(0.1)

