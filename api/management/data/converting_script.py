import json


def convert_data(data):
    """Конвертирует список объектов в формат parameter.json."""
    parameters = []
    for item in data:
        parameters.append(
            {
                "unit": None,
                "toolmodule": item["sn_"],
                "parameter_type": "dbtlength",
                "parameter_value": item["dbtlength"],
            }
        )
        parameters.append(
            {
                "unit": None,
                "toolmodule": item["sn_"],
                "parameter_type": "dbtweight",
                "parameter_value": item["dbtweight"],
            }
        )
        parameters.append(
            {
                "unit": None,
                "toolmodule": item["sn_"],
                "parameter_type": "dbtmax_od_",
                "parameter_value": item["dbtmax_od_"],
            }
        )
        parameters.append(
            {
                "unit": None,
                "toolmodule": item["sn_"],
                "parameter_type": "dbtmax_od_collapsed_",
                "parameter_value": item["dbtmax_od_collapsed_"],
            }
        )
        parameters.append(
            {
                "unit": None,
                "toolmodule": item["sn_"],
                "parameter_type": "dbtmax_od_opened_",
                "parameter_value": item["dbtmax_od_opened_"],
            }
        )
        parameters.append(
            {
                "unit": None,
                "toolmodule": item["sn_"],
                "parameter_type": "dbtimage_h_shift",
                "parameter_value": item["dbtimage_h_shift"],
            }
        )
        parameters.append(
            {
                "unit": None,
                "toolmodule": item["sn_"],
                "parameter_type": "dbtimage_h_scale",
                "parameter_value": item["dbtimage_h_scale"],
            }
        )
        parameters.append(
            {
                "unit": None,
                "toolmodule": item["sn_"],
                "parameter_type": "dbtimage_h_y1",
                "parameter_value": item["dbtimage_h_y1"],
            }
        )
        parameters.append(
            {
                "unit": None,
                "toolmodule": item["sn_"],
                "parameter_type": "dbtimage_h_y2",
                "parameter_value": item["dbtimage_h_y2"],
            }
        )
        parameters.append(
            {
                "unit": None,
                "toolmodule": item["sn_"],
                "parameter_type": "dbtcomp_str",
                "parameter_value": item["dbtcomp_str"],
            }
        )
    return parameters


# Загрузите данные из JSON-файла или из переменной
with open("Base/tool_module.json", "r") as f:
    data = json.load(f)

# Конвертируйте данные в формат parameter.json
parameters = convert_data(data)

# Сохраните результаты в новый файл
with open("Base/parameter.json", "w") as f:
    json.dump(parameters, f, indent=4)

print("Данные успешно конвертированы в parameter.json!")


# import json
#
#
# def remove_empty_lines(file_path):
#     """Удаляет пустые строки из JSON-файла."""
#     with open(file_path, "r") as f:
#         data = json.load(f)
#
#     # Удаляем пустые строки из "dbcomment_"
#     for item in data:
#         item["dbcomment_"] = item["dbcomment_"]
#
#     # Сохраняем изменения в файл
#     with open(file_path, "w") as f:
#         json.dump(data, f, indent=4)
#
#
# # Замените "data.json" на путь к вашему файлу
# remove_empty_lines("tool_module.json")
