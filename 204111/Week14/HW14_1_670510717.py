#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# 670510717
# HW14_1
# 204111 Sec 003


def main():
    # infile_name = append_ranking()
    append_ranking()
    # pass

def append_ranking(infile_name: str='score_in.txt', outfile_name: str='score_out.txt'):
    with open(infile_name, 'rt', encoding='utf-8') as fin:
        txt = fin.read()
    # อ่านข้อมูลจากไฟล์ที่ระบุชื่อด้วยตัวแปร infile_name
    txt = txt.strip()
    txt = txt.split('\n')
    temp = {}
    for line in txt:
        no_none = line.replace('None', '0')
        list_i = no_none.split()
        for i in range(1,len(list_i)):
            list_i[i] = float(list_i[i])
        list_i += [sum(sorted(list_i[1:])[1:3])]
        temp[list_i[0]] = list_i[-1]
    # จัด rank
    rank_up = sorted(temp, key=lambda x: temp[x])[::-1]
    # เพิ่ม rank
    for rank in range(len(rank_up)):
        temp[rank_up[rank]] = rank + 1
        # for j in range(len(rank_up[rank])):
            # if rank_up[rank][j] == 0:
            #     rank_up[rank][j] = 'None'
            # else:
            #     rank_up[rank][j] = str(rank_up[rank][j])
        # rank_up[rank] = ' '.join(rank_up[rank])
    # rank_up = list(map(lambda x: x + [rank_up[]],txt))
    result = list(map(lambda x: x + " " + str(temp[x[:9]]), txt))
    result = '\n'.join(result)
    with open(outfile_name, 'wt') as fout:
        fout.write(result)
    # return rank_up

    # print(rank_up)


        # print(type(list_i[1]))
        # print(i[1])
    # เขียนผลลัพธ์ลงในไฟล์ที่มีชื่อระบุด้วยตัวแปร outfile_name
    # เพิ่ม ด้รับไว้ที่ส่วนท้ายของแต่ละบรรทัด


if __name__ == '__main__':
    main()