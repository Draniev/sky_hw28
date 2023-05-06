import json
import csv


def save_csv_to_json(csv_list: list):
    csv_lines = []
    for csv_file, model_name in csv_list:
        with open(csv_file, 'r') as file:
            csv_data = csv.DictReader(file)
            for row in csv_data:
                # Преобразование специфического параметра из str в bool
                if row.get('is_published'):
                    row['is_published'] = True if row['is_published'] == 'TRUE' else False
                # Сохранение в формат фикстуры для загрузки manage.py loaddata filename.json
                json_dict = {'model': model_name,
                             'pk': row.pop('id'),
                             'fields': row}

                csv_lines.append(json_dict)
                print(json_dict)
                print(row)

        json_file = csv_file[:-3] + 'json'
        with open(json_file, 'w') as file:
            json.dump(csv_lines, file, ensure_ascii=False)


if __name__ == '__main__':
    csv_list = [
        ('../datasets/categories.csv', 'categories.CatModel'),
        ('../datasets/ads.csv', 'ads.AdsModel'),
    ]

    save_csv_to_json(csv_list)

