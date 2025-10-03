import matplotlib.pyplot as plt
from collections import defaultdict

with open("LOG", "r") as f:
    data = f.read()

# Словарь для хранения результатов по каждому методу
# {метод: ([sizes], [values])}
results = defaultdict(lambda: ([], []))

for line in data.strip().splitlines():
    parts = line.split()
    
    # Предполагаем, что формат строки: "MethodName:Size Value1 Value2 ..."
    # Например: "Sequential:100 0.0012 1.5"
    try:
        method, size_str = parts[0].split(":")
        size = int(size_str)
        val = float(parts[1])  # берем первое число после размера
    except (ValueError, IndexError) as e:
        # Пропускаем или логируем некорректно отформатированные строки
        print(f"Skipping malformed line: {line} (Error: {e})")
        continue
    
    sizes, vals = results[method]
    sizes.append(size)
    vals.append(val)

# --- Блок построения графиков ---
plt.figure(figsize=(10, 6)) # Увеличим размер для лучшей читаемости

# Строим графики для каждого метода
for method, (sizes, vals) in results.items():
    # Важно: отсортировать данные перед построением,
    # чтобы линия на графике была корректной.
    sorted_data = sorted(zip(sizes, vals))
    sorted_sizes, sorted_vals = zip(*sorted_data)
    
    plt.plot(sorted_sizes, sorted_vals, marker="o", linestyle='-', label=method)

# Установка логарифмического масштаба для оси X (размер матрицы)
plt.xscale('log')

# Дополнительно, полезно установить и логарифмический масштаб для оси Y (время),
# чтобы лучше видеть различия между методами, если время сильно отличается.
# Вы можете раскомментировать эту строку, если это необходимо:
# plt.yscale('log') 

plt.xlabel("Matrix size (log scale)")
plt.ylabel("Time (s)")
plt.title("Matrix multiplication timings (Log X)")
plt.legend()
plt.grid(True, which="both", ls="-", alpha=0.6) # Отображаем сетку для обеих сеток логарифмического масштаба

plt.show()
plt.savefig("result.png")