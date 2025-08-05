import os
import stat
import sys
from errno import EACCES, EPERM
from shutil import rmtree as shutil_rmtree


def rmtree(path):
    kwargs = {}
    if sys.platform == "win32":
        kwargs["onerror"] = _onerror_windows
    return shutil_rmtree(path, **kwargs)


def _onerror_windows(function, path, excinfo):
    if isinstance(excinfo[1], OSError) and excinfo[1].errno in (EACCES, EPERM):
        os.chmod(path, stat.S_IWRITE)
        function(path)
