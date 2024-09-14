check_num = (newwy[0] * 13) + (newwy[1] * 12) + (newwy[2] * 11) + (newwy[3] * 10) + (newwy[4] * 9) + 
(newwy[5] * 8) + (newwy[6] * 7) + (newwy[7] * 6) + (newwy[8] * 5) + (newwy[9] * 4) + (newwy[10] * 3) + (newwy[11] * 2)

check_num = (check_num % 11)[-1]

list_check = list(map(lambda x:(((x[0] * 13) + (x[1] * 12) + (x[2] * 11) + (x[3] * 10) + (x[4] * 9) + 
    (x[5] * 8) + (x[6] * 7) + (x[7] * 6) + (x[8] * 5) + (x[9] * 4) + (x[10] * 3) + (x[11] * 2)) % 11)[-1], no_dash ))



    # list_check = list(map(lambda x:(((x[0] * 13) + (x[1] * 12) + (x[2] * 11) + (x[3] * 10) + (x[4] * 9) + 
    # (x[5] * 8) + (x[6] * 7) + (x[7] * 6) + (x[8] * 5) + (x[9] * 4) + (x[10] * 3) + (x[11] * 2)) % 11)[-1], no_dash ))

    # correct = list(filter(lambda x:str(x)[-1] == list_check, list_id))