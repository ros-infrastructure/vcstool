import logging
import os

from flake8 import configure_logging
from flake8.main.application import Application
from pydocstyle.config import log

log.level = logging.INFO


def test_flake8():
    configure_logging(1)
    argv = [
        '--extend-ignore=' + ','.join([
            'A003', 'D100', 'D101', 'D102', 'D103', 'D104', 'D105', 'D107']),
        '--exclude', 'vcstool/compat/shutil.py',
        '--import-order-style=google'
    ]
    base_path = os.path.join(os.path.dirname(__file__), '..')
    paths = [
        os.path.join(base_path, 'test'),
        os.path.join(base_path, 'vcstool'),
    ]
    scripts_path = os.path.join(base_path, 'scripts')
    for script in os.listdir(scripts_path):
        if script.startswith('.'):
            continue
        paths.append(os.path.join(scripts_path, script))

    app = Application()
    app.run(argv + paths)
    assert app.result_count == 0, \
        f'Found {app.result_count} code style warnings'


if __name__ == '__main__':
    test_flake8()
