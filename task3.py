import sys

def parse_log_line(line: str) -> dict: # Розбираємо рядок з логу
    parts = line.strip().split()
    if len(parts) < 4:
        return {}
    return {
        "date": parts[0],
        "time": parts[1],
        "level": parts[2], # Рівень логування
        "message": " ".join(parts[3:])
    }


def load_logs(file_path: str) -> list:
    logs = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                log = parse_log_line(line)
                if log:
                    logs.append(log)
    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено.")
        sys.exit(1)
    return logs


def count_logs_by_level(logs: list) -> dict:
    counts = {}
    for log in logs:
        level = log["level"].upper()
        counts[level] = counts.get(level, 0) + 1
    return counts


def display_log_counts(counts: dict):
    print("\nРівень логування  |  Кількість")
    print("------------------|-----------")
    for level, count in counts.items():
        print(f"{level:<17} |  {count}")


def filter_logs_by_level(logs: list, level: str) -> list: # Відбираємо тільки ті записи, які відповідають потрібному рівню
    return [log for log in logs if log["level"].lower() == level.lower()]

if __name__ == "__main__": #Перевірка аргументів
    if len(sys.argv) < 2:
        print("Приклад використання: python task3.py <шлях_до_логу> [рівень]")
        sys.exit(1)

    path_to_log = sys.argv[1]
    level_to_filter = sys.argv[2] if len(sys.argv) > 2 else None
    log_entries = load_logs(path_to_log)
    level_stats = count_logs_by_level(log_entries) # Підрахунок
    display_log_counts(level_stats) # Статистика

    if level_to_filter:
        filtered = filter_logs_by_level(log_entries, level_to_filter)
        print(f"\nДеталі для рівня '{level_to_filter.upper()}':")
        for log in filtered:
            print(f"{log['date']} {log['time']} -> {log['message']}")


