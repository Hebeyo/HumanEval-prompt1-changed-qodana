def valid_date(date):
    if date == '':
        return False
    if len(date) != 10:
        return False
    if date[2] != '-' or date[5] != '-':
        return False
    month, day, year = date.split('-')
    if len(month) != 2 or len(day) != 2 or len(year) != 4:
        return False
    if not month.isdigit() or not day.isdigit() or not year.isdigit():
        return False
    month, day, year = int(month), int(day), int(year)
    if month < 1 or month > 12:
        return False
    if month in [1,3,5,7,8,10,12] and (day < 1 or day > 31):
        return False
    if month in [4,6,9,11] and (day < 1 or day > 30):
        return False
    if month == 2 and (day < 1 or day > 29):
        return False
    return True
