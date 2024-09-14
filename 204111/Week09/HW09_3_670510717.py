#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# HW09_3
# 204111 Sec 003


def main():
    # print(check_back('1-2345-67890-12-1'))
    test()


def check_back(id_str):
    if id_str[0] == str(0):
        return False

    sum_id = (
        (int(id_str[0]) * 13)
        + (int(id_str[2]) * 12)
        + (int(id_str[3]) * 11)
        + (int(id_str[4]) * 10)
        + (int(id_str[5]) * 9)
        + (int(id_str[7]) * 8)
        + (int(id_str[8]) * 7)
        + (int(id_str[9]) * 6)
        + (int(id_str[10]) * 5)
        + (int(id_str[11]) * 4)
        + (int(id_str[13]) * 3)
        + (int(id_str[14]) * 2)
    )

    mod_id = sum_id % 11
    # print(mod_id)
    # if mod_id == 10:
    #     minus_id = str(0)
    # else:
    minus_id = 11 - mod_id
    # print(minus_id)
    check_id = str(minus_id)[-1] == id_str[-1]

    # how to check = https://memo8.com/check-digit-thai-citizen-id-validator

    return check_id


def unmask_id(masked_id: str) -> list[str]:
    num = masked_id.count("*")

    # fill 0 ตามจำนวน "*" เพื่อให้นำไป format ได้ทุกตัว >>> EX: ['00', '01', '02', '03', '04', '05']
    ranger = list(map(lambda x: str(x).zfill(num), list(range(10**num))))

    # แปลง "*" -> "{}" เพื่อเเอาไปใช้ในการ format >>> EX: "1-2345-67890-1{}-{}"
    id_ = "".join(
        list(
            map(
                lambda x: x.replace(
                    "*",
                    "{}",
                ),
                masked_id,
            )
        )
    )

    # เติม ตัวเลขแต่ละชุด ใส่ใน "1-2345-67890-1{}-{}" >>> EX: ['1-2345-67890-10-0', '1-2345-67890-10-1', '1-2345-67890-10-2']
    list_id = list(map(lambda x: id_.format(*x), ranger))
    # print(list_id)

    check_id = list(filter(lambda x: check_back(x), list_id))

    # print(check_id)
    return check_id


def test():
    assert sorted(unmask_id("1-2345-67890-1*-*")) == sorted(
        [
            "1-2345-67890-10-4",
            "1-2345-67890-11-2",
            "1-2345-67890-12-1",
            "1-2345-67890-13-9",
            "1-2345-67890-14-7",
            "1-2345-67890-15-5",
            "1-2345-67890-16-3",
            "1-2345-67890-17-1",
            "1-2345-67890-18-0",
            "1-2345-67890-19-8",
        ]
    )

    print("Let's go to sleep")


if __name__ == "__main__":
    main()
