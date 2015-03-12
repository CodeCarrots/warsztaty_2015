dates_lst = ['2015-02-21', '2015-02-27', '2015-02-24', '2015-02-25', '2015-02-26', '2015-03-10', '2015-03-12', '2015-02-16', '2015-02-05', '2015-02-23', '2015-02-15', '2015-02-08', '2015-02-14', '2015-03-01', '2015-02-17', '2015-02-28', '2015-02-18', '2015-03-06', '2015-03-11', '2015-03-03', '2015-03-14', '2015-02-10', '2015-02-12', '2015-03-15', '2015-03-04', '2015-03-05', '2015-02-22', '2015-03-02', '2015-03-09', '2015-03-13', '2015-03-07', '2015-02-20', '2015-02-03', '2015-02-13', '2015-02-11', '2015-02-04', '2015-02-19', '2015-02-06', '2015-02-07', '2015-02-09', '2015-03-16', '2015-03-08']

# struktura liczników: [<all>, <feb>, <mar>]
dates_counters = [0, 0, 0]
for date in dates_lst:
    # all_cnt, feb_cnt, mar_cnt = dates_counters
    all_cnt = dates_counters[0]
    feb_cnt = dates_counters[1]
    mar_cnt = dates_counters[2]

    if date >= '2015-03-01':
        mar_cnt += 1
    elif date >= '2015-02-01':
        feb_cnt += 1
    all_cnt += 1

    dates_counters[0] = all_cnt
    dates_counters[1] = feb_cnt
    dates_counters[2] = mar_cnt

#    dates_counters[0], dates_counters[1], dates_counters[2] = all_cnt, feb_cnt, mar_cnt

#    dates_counters = [all_cnt, feb_cnt, mar_cnt]

# 42
print('Ilość dni objęta statystyką:', dates_counters[0])
# 26
print('- w tym w lutym 2015:', dates_counters[1])
# 16
print('- w tym w marcu 2015:', dates_counters[2])


# problemy: dużo danych, dużo zmiennych, brak dokumentacji opisującej działanie
