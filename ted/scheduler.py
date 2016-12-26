

class SchedulerConfig(object):
    JOBS = [
        {
            'id': 'call_parents_reminder_weekday',
            'func': 'ted.views:call_parents_reminder',
            'trigger': 'cron',
            'day_of_week': '0-4', #mon-fri
            'hour': 19, #7pm
            'minute': 30,
            'timezone': 'America/Los_Angeles'
        },
        {
            'id': 'call_parents_reminder_weekend',
            'func': 'ted.views:call_parents_reminder',
            'trigger': 'cron',
            'day_of_week': '5-6', #sat-sun
            'hour': 16, #4pm
            'minute': 0,
            'timezone': 'America/Los_Angeles'
        }
    ]
    SCHEDULER_VIEWS_ENABLED = True


    # test job below
    # {
    #     'id': 'test',
    #     'func': 'ted.views:call_parents_reminder',
    #     'trigger': 'cron',
    #     'day_of_week': '0-6',
    #     'hour': 13,
    #     'minute': 15,
    #     'timezone': 'America/Los_Angeles'
    # }


# from apscheduler.schedulers.blocking import BlockingScheduler

# sched = BlockingScheduler()

# @sched.scheduled_job('interval', minutes=3)
# def timed_job():
#     print('This job is run every three minutes.')

# @sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)
# def scheduled_job():
#     print('This job is run every weekday at 5pm.')

# sched.start()