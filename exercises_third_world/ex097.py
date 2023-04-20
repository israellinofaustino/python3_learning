def different_print(msg):
    len_ = len(msg) + 2
    print('^' * len_)
    print(msg.center(len_))
    print('^' * len_)


different_print('Hello!')
different_print('Israel Faustino')
different_print('Israel')
