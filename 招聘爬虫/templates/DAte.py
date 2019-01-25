"""
1. 学习目标
    1.1  
"""
import datetime

if __name__ == "__main__":
    now = datetime.datetime.now()
    delta = datetime.timedelta(days=7)
    n_days = now - delta
    print(n_days.strftime('%Y%m%d')+"-"+now.strftime('%Y%m%d'))