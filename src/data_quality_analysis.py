import pandas as pd
import datetime
from data_load import load_data


def analyze_quality(df):
    """
    пошук пропусків та аномалій.
    """
    if df is None or df.empty:
        print("Немає даних для аналізу.")
        return

    print("--- Аналіз якості даних ---")

    # 1. Пошук пропущених значень
    print("\n1. Пропущені значення по колонках:")
    missing = df.isnull().sum()
    missing_filtered = missing[missing > 0]
    if not missing_filtered.empty:
        print(missing_filtered)
    else:
        print("Пропущених значень не виявлено.")

    # 2. Аномалії в колонці MAKE_YEAR (Рік випуску)
    if 'MAKE_YEAR' in df.columns:
        current_year = datetime.datetime.now().year
        anomalies_year = df[(df['MAKE_YEAR'] < 1900) | (df['MAKE_YEAR'] > current_year)]
        print(f"\n2. Аномальні роки випуску (< 1900 або > {current_year}):")
        print(f"Знайдено записів: {len(anomalies_year)}")
        if not anomalies_year.empty:
            print("Приклади аномалій:")
            print(anomalies_year[['BRAND', 'MODEL', 'MAKE_YEAR']].head())

    print("\n3. Перевірка технічних показників (нульові значення):")
    cols_to_check = ['CAPACITY', 'OWN_WEIGHT', 'TOTAL_WEIGHT']
    for col in cols_to_check:
        if col in df.columns:
            zero_count = len(df[df[col] == 0])
            print(f"Нульових значень у колонці {col}: {zero_count}")


if __name__ == "__main__":
    data = load_data()
    analyze_quality(data)