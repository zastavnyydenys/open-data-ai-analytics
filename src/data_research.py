import pandas as pd
import datetime
from data_load import load_data


def conduct_research(df):

    if df is None or df.empty:
        print("Немає даних для дослідження.")
        return

    print("--- Дослідження та перевірка гіпотез ---")

    # --- Перевірка Гіпотези 1 ---
    print("\nГіпотеза 1: Топ-3 марки авто займають понад 30% ринку.")
    if 'BRAND' in df.columns:
        total_cars = len(df)
        # Рахуємо кількість авто кожної марки і беремо топ-3
        top_3_counts = df['BRAND'].value_counts().head(3)
        top_3_total = top_3_counts.sum()
        percentage = (top_3_total / total_cars) * 100

        print(f"Топ-3 марки:\n{top_3_counts.to_string()}")
        print(f"Частка Топ-3 на ринку: {percentage:.2f}%")

        if percentage > 30:
            print("Висновок: Гіпотеза 1 ПІДТВЕРДЖЕНА!")
        else:
            print("Висновок: Гіпотеза 1 СПРОСТОВАНА.")
    else:
        print("Колонка BRAND відсутня у датасеті.")

    # --- Перевірка Гіпотези 2 ---
    print("\nГіпотеза 2: Більше половини авто в базі мають вік старше 10 років.")
    if 'MAKE_YEAR' in df.columns:
        current_year = datetime.datetime.now().year
        # Спочатку відфільтруємо аномалії, які ми знайшли в попередньому модулі
        valid_cars = df[(df['MAKE_YEAR'] >= 1900) & (df['MAKE_YEAR'] <= current_year)]
        total_valid = len(valid_cars)

        # Рахуємо авто, які випущені більше ніж 10 років тому
        older_than_10 = valid_cars[valid_cars['MAKE_YEAR'] < (current_year - 10)]
        older_count = len(older_than_10)

        if total_valid > 0:
            older_percentage = (older_count / total_valid) * 100
            print(f"Загальна кількість валідних авто: {total_valid}")
            print(f"З них старше 10 років: {older_count}")
            print(f"Відсоток старих авто: {older_percentage:.2f}%")

            if older_percentage > 50:
                print("Висновок: Гіпотеза 2 ПІДТВЕРДЖЕНА!")
            else:
                print("Висновок: Гіпотеза 2 СПРОСТОВАНА.")
    else:
        print("Колонка MAKE_YEAR відсутня у датасеті.")


if __name__ == "__main__":
    data = load_data()
    conduct_research(data)