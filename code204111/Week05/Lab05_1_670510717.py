#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# 670510717
# Lec05_1
# 204111 Sec 003


import string

def main():
    # text = str(input(""))
    # c = str(input(""))
    # print(palindrome_without(text, c))
    test_palindrome_without()
    
    
def palindrome_without(text: str, c: str) -> bool:
    #Cc cc -> cccc
    text_lower = text.lower()                           # ทำข้อความให้เป็นพิมพ์เล็กทั้งหมด
    text_non_space = text_lower.replace(' ', '')        # ลบ space ออก
    
    # replace('C','')
    new_text = text_non_space.replace(c, '')            # แทนอักษรที่ต้องการลบเป็น ''
    
    check_new_text = new_text[-1::-1]                   # เช็คคำว่าอ่านย้อนกลับแล้วเป็นคำเดิมนะ 
    
    if new_text == '':                                  # ถ้าคำใหม่เป็นสตริงเปล่า
        return False
        
    
    if check_new_text == new_text:                      # ถ้าคำใหม่กลับคำหน้าหลังแล้วเหมือนกับคำที่ลบ space ออก
        return True
        
    else:                                               # ถ้าคำใหม่กลับคำหน้าหลังแล้วไม่เหมือนกับคำที่ลบ space ออก
        return False
    

def test_palindrome_without():
   assert palindrome_without("Banana", "b") is True
   assert palindrome_without("Swap of paws", "f") is True
   assert palindrome_without("T", "t") is False
   print("all ok!")
    
    
if __name__ == '__main__':
    #print("C"=='c')
    main()