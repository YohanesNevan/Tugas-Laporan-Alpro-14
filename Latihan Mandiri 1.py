import re
from datetime import datetime

txt = """
Pada tanggal 1945-08-17 Indonesia merdeka. Indonesia memiliki beberapa pahlawan
nasional, seperti Pangeran Diponegoro (TL: 1785-11-11), Pattimura (TL: 1783-06-08) dan Ki
Hajar Dewantara (1889-05-02).
"""

dates = re.findall(r'\b\d{4}-\d{2}-\d{2}\b', txt)
now = datetime.now()

for date_str in dates:
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    delta = now - date_obj
    formatted_date = date_obj.strftime('%d-%m-%Y')
    print(f"{date_obj} selisih {delta.days} hari")
