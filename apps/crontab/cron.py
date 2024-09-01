from apps.mailing.management.commands.run_mailing import Command


def scheduled_mailing():
    Command().handle()
