import datetime
from PythonFiles import change_time_format

datee = datetime.date(1992, 2, 10)
print(datee)

a = str(change_time_format.convert_time('২', 'জুন', '১৯৯৫'))
print(a)