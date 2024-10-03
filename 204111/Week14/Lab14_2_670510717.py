#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# 670510717
# Lab14_2
# 204111 Sec 003

def main():
    list_x = [('11/Jan/1900', 'Event A'), ('5/Dec/2001', 'Event B'),
    ('5/Dec/2002', 'Event C'), ('21/Aug/2008', 'Event D'),
    ('9/Mar/2013', 'Event E'), ('11/Mar/2017', 'Event F'),
    ('7/May/2019', 'Event G'), ('29/Feb/2032', 'Event H'),
    ('9/Nov/2042', 'Event I')]
    event = search_event(list_x, '23/Aug/2008', show_steps=True)
    print('---')
    print(event)
def less_than(date1, date2):
    months_dict = {
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "May": 5,
    "Jun": 6,
    "Jul": 7,
    "Aug": 8,
    "Sep": 9,
    "Oct": 10,
    "Nov": 11,
    "Dec": 12
    }

    day1, month1, year1 = date1.split('/')
    day2, month2, year2 = date2.split('/')
    d1 = int(day1)
    d2 = int(day2)
    m1 = months_dict[month1]
    m2 = months_dict[month2]
    y1 = int(year1)
    y2 = int(year2)
    if y1 > y2:
        return False
    elif y1 == y2:
        if m1 > m2:
            return False
        elif m1 == m2:
            if d1 > d2:
                return False
    return True

def search_event(list_x: list[tuple[str]], key: str, show_steps: bool=False) -> tuple[str] | None:
    lo = 0
    hi = len(list_x) - 1
    found = None
    while lo <= hi and not found:
        mid = (lo + hi) // 2
        # print(key, list_x[mid])
        if key == list_x[mid][0]:
            found = list_x[mid]
        elif less_than(key, list_x[mid][0]):
            hi = mid - 1
        else:
            lo = mid + 1
        if show_steps is True:
            print(( f"{[mid]}: {list_x[mid][0]}"))
    return found


if __name__ == '__main__':
    main()