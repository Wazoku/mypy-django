from typing import Optional

import datetime

def parse_date(value: str) -> Optional[datetime.date]:
    ...

def parse_time(value: str) -> Optional[datetime.time]:
    ...

def parse_datetime(value: str) -> Optional[datetime.datetime]:
    ...

def parse_duration(value: str) -> Optional[datetime.timedelta]:
    ...
