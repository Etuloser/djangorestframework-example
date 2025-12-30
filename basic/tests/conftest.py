"""
通过命令:
python manange.py dumpdata > tests\my_fixture_data.json
来从默认数据库收集数据到文件
"""

import pytest
from django.core.management import call_command


@pytest.fixture(scope="session")
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command("loaddata", "tests\my_fixture_data.json")
