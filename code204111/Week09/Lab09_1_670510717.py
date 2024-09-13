#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# HW09_2
# 204111 Sec 003


def main():
    patterned_message(
        "Three Diamonds!",
        """ 
    *     *     * 
   ***   ***   *** 
  ***** ***** ***** 
   ***   ***   *** 
    *     *     * 
""",
    )


# ('''T     h     r
#    eeD   iam   ond
#   s!Thr eeDia monds
#    !Th   ree   Dia
#     m     o     n ''')


def patterned_message(message: str, pattern: str, start=0, result="") -> None:
    message = message.replace(" ", "")
    if len(pattern) == len(result):
        print(result)
        return result
    if pattern[start] == "*":  # ถ้าตำแหน่งนั้นเจอ "*"
        result = result + message[0]  # ให้ result เก็บตำแหน่งนั้นด้วย message ตำแหน่งที่ 0
        message = (message[1:] + message[0])  # วน message -> ThreeDiamonds! -> hreeDiamonds!T
    else:
        result = result + pattern[start]  # ให้ result เก็บตำแหน่งนั้นไว้เหมือนเดิม
        message = message  # ไม่หมุนตัวแปลงค่า

    return patterned_message(message, pattern, start + 1, result)


if __name__ == "__main__":
    main()
