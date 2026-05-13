import os
import matplotlib.pyplot as plt
from data_load import load_data


def visualize_data(df):
    if df is None or df.empty:
        print("Немає даних для візуалізації.")
        return

    print("--- Генерація візуалізацій ---")

    if 'BRAND' in df.columns:
        print("Будуємо графік: Топ-10 марок авто...")

        # Беремо топ-10 марок
        top_10 = df['BRAND'].value_counts().head(10)


        plt.figure(figsize=(10, 6))
        top_10.plot(kind='bar', color='skyblue', edgecolor='black')
        plt.title('Топ-10 найпопулярніших марок зареєстрованих авто', fontsize=14)
        plt.xlabel('Марка автомобіля', fontsize=12)
        plt.ylabel('Кількість реєстрацій', fontsize=12)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

        output_dir = os.path.join("artifacts", "visualization")
        os.makedirs(output_dir, exist_ok=True)


        output_path = os.path.join(output_dir, "top_10_brands.png")
        plt.savefig(output_path)
        print(f" Графік успішно збережено за шляхом: {output_path}")
    else:
        print("Колонка BRAND відсутня, неможливо побудувати графік.")


if __name__ == "__main__":
    data = load_data()
    visualize_data(data)