import asyncio
import logging

from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "A bot resumes complaints"

    async def main(self):
        from tg_bot import config
        logging.basicConfig(level=logging.INFO)
        await config.dispatcher.start_polling(config.bot)

    def handle(self, *args, **options):
        asyncio.run(self.main())
