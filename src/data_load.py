import pandas as pd
import sys
import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


if os.environ.get("USE_LOCAL_DATA") == "true":
    print("[ENV: SELF-HOSTED] Використовуємо великий локальний датасет.")
    DEFAULT_PATH = Path("D:/DevOps/open-data-ai-analytics/data/raw/dataset.csv")

elif os.environ.get("CI") == "true":
    print(" [ENV: CLOUD CI] Використовуємо маленький тестовий датасет.")
    DEFAULT_PATH = BASE_DIR / "data" / "raw" / "test_data.csv"
else:
    print("[ENV: LOCAL RUN] Запуск вручну з PyCharm.")
    DEFAULT_PATH = BASE_DIR / "data" / "raw" / "dataset.csv"

def load_data(file_path=DEFAULT_PATH):

    print(f"Спроба завантажити дані з: {file_path}")


    if not os.path.exists(file_path):
        print(f"Помилка: Файл не знайдено за шляхом {file_path}")
        return None

    try:

        df = pd.read_csv(
            file_path,
            sep=None,
            engine='python',
            encoding='utf-8',
            on_bad_lines='skip'
        )

        print(f"Успішно завантажено. Розмір датасету: {df.shape}")

        if df.shape[1] <= 1:
            print("Попередження: Датасет містить лише одну колонку. Спробуйте вказати розділювач жорстко!")

        return df

    except Exception as e:
        print(f"Критична помилка під час читання файлу: {e}")
        return None


if __name__ == "__main__":
    data = load_data()

    if data is not None:
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', 1000)

        print("\nПерші 3 рядки даних:")
        print(data.head(3))

        print("\nДоступні колонки:")
        print(list(data.columns))
    else:
        print("\n Дані не завантажились. Перевірте налаштування середовища.")
        sys.exit(1)