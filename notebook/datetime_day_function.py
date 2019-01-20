import datetime

dt = datetime.datetime(2018, 1, 1)
print(dt)
# 2018-01-01 00:00:00

print(dt.weekday())
# 0

print(type(dt.weekday()))
# <class 'int'>

print(dt.isoweekday())
# 1

print(type(dt.isoweekday()))
# <class 'int'>

w_list = ['月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日', '日曜日']
print(w_list[dt.weekday()])
# 月曜日

def get_day_of_week_jp(dt):
    w_list = ['月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日', '日曜日']
    return(w_list[dt.weekday()])

print(get_day_of_week_jp(dt))
# 月曜日

dt2 = datetime.datetime(2018, 1, 2)
print(dt2)
# 2018-01-02 00:00:00

print(get_day_of_week_jp(dt2))
# 火曜日

s = '2018年1月10日'
print(get_day_of_week_jp(datetime.datetime.strptime(s, '%Y年%m月%d日')))
# 水曜日

def get_day_of_week_jp_s(s):
    return get_day_of_week_jp(datetime.datetime.strptime(s, '%Y年%m月%d日'))

print(get_day_of_week_jp_s(s))
# 水曜日

def get_month_jp(dt):
    m_list = [None, '睦月', '如月', '弥生', '卯月', '皐月', '水無月', '文月', '葉月', '長月', '神無月', '霜月', '師走']
    return(m_list[dt.month])

print(get_month_jp(dt2))
# 睦月
