from apscheduler.schedulers.blocking import BlockingScheduler

# 定义一个job类，完成想要做的事
def worker():
    print("hello scheduler")

# 定时每分钟第3秒和第5秒执行任务second = '3,5'
# 定时每分钟第3秒至第5秒执行任务second = '3-5'
schedudler = BlockingScheduler()
schedudler.add_job(worker,'cron',second = '20,30')
# schedudler.add_job(worker,'cron', hour = '6,11,15')

schedudler.start() # 开始任务