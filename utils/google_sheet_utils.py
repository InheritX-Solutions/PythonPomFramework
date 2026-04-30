import requests


class GoogleSheetUtils:

    @staticmethod
    def get_data(sheet_id):
        url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv"
        response = requests.get(url)

        lines = response.text.strip().split("\n")

        headers = [
            h.strip().replace("\ufeff", "").replace('"', '').lower()
            for h in lines[0].split(",")
        ]

        data = []
        for row in lines[1:]:
            if row.strip() == "":
                continue

            values = [
                v.strip().replace('"', '')
                for v in row.split(",")
            ]

            row_dict = dict(zip(headers, values))
            data.append(row_dict)

        return data