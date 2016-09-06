
# # from run import app
# from flask_apscheduler import APScheduler


# class Config(object):
#     JOBS = [
#         {
#             'id': 'call_parents_reminder_weekday',
#             'func': 'run:call_parents_reminder',
#             'trigger': 'cron',
#             'day_of_week': '0-4',
#             'hour': 19, #7pm
#             'minute': 30,
#             'timezone': 'America/Los_Angeles'
#         },
#         {
#             'id': 'call_parents_reminder_weekend',
#             'func': 'run:call_parents_reminder',
#             'trigger': 'cron',
#             'day_of_week': '5-6',
#             'hour': 16, #4pm
#             'minute': 0,
#             'timezone': 'America/Los_Angeles'
#         }
#     ]
#     SCHEDULER_VIEWS_ENABLED = True



# app.config.from_object(Config())
# scheduler = APScheduler()
# scheduler.init_app(app)
# print "starting scheduler"
# scheduler.start()


from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=3)
def timed_job():
    print('This job is run every three minutes.')

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)
def scheduled_job():
    print('This job is run every weekday at 5pm.')

sched.start()