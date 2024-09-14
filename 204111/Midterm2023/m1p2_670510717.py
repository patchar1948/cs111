#!/usr/bin/env python3
# Patcharin
# 670510717
# Sec003


def transform_id(int_id):
    return str(int_id)[-3:] + '-' + str(int_id)[0:2]


if __name__ == '__main__':
    assert transform_id(650241555) == '555-65'
    print("All OK!")