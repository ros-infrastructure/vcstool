vcs2l_clients = []

try:
    from .bzr import BzrClient
    vcs2l_clients.append(BzrClient)
except ImportError:
    pass

try:
    from .git import GitClient
    vcs2l_clients.append(GitClient)
except ImportError:
    pass

try:
    from .hg import HgClient
    vcs2l_clients.append(HgClient)
except ImportError:
    pass

try:
    from .svn import SvnClient
    vcs2l_clients.append(SvnClient)
except ImportError:
    pass

try:
    from .tar import TarClient
    vcs2l_clients.append(TarClient)
except ImportError:
    pass

try:
    from .zip import ZipClient
    vcs2l_clients.append(ZipClient)
except ImportError:
    pass

_client_types = [c.type for c in vcs2l_clients]
if len(_client_types) != len(set(_client_types)):
    raise RuntimeError(
        'Multiple vcs clients share the same type: ' +
        ', '.join(sorted(_client_types)))
