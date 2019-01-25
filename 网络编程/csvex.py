import csv

DATA = (
    (u'学科编号', u'学科', u'开班时间', u'预计人数'),
    (u'1', u'Java', u'2018/8/9', u'50'),
    ('2', 'PHP', '2018/8/10', '51'),
    ('3', 'UI', '2018/8/11', '52'),
    ('4', 'H5', '2018/8/12', '53'),
    ('5', 'Python', '2018/8/13', '54'),
)

print('*** 保存CSV数据')
f = open('xueke.csv', 'w', newline='')
writer = csv.writer(f)
for record in DATA:
    writer.writerow(record)
f.close()

print('*** 读取CSV数据')
f = open('xueke.csv', 'r', newline='')
reader = csv.reader(f)
for no, name, time, num in reader:
    print('%s  %s  %s  %s' % (no, name, time, num))
f.close()
