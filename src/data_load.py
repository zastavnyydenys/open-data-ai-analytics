import pandas as pd


def load_data(file_path="../data/raw/dataset.csv"):

    print(f"Спроба завантажити дані з: {file_path}")

    try:
        df = pd.read_csv(file_path, encoding='utf-8', sep=';', on_bad_lines='skip', low_memory=False)
        print(f"Успішно завантажено. Розмір датасету: {df.shape}")
        return df
    except Exception as e:
        print(f"Помилка читання файлу: {e}")
        return None


if name == "main":
    data = load_data()

    if data is not None:

        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', 1000)

        print("\nПерші 3 рядки даних:")
        print(data.head(3))
    else:
        print("\nДані не завантажились. Перевірте наявність файлу.")