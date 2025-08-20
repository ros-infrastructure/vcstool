^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package vcs2l
^^^^^^^^^^^^^^^^^^^^^^^^^^^

1.1.3 (2025-08-20)
------------------
* Fix: UnboundLocalError: local variable 'version_type' referenced before assignment (`#15 <https://github.com/ros-infrastructure/vcs2l/pull/15>`_)
* Enabled command retry on vcs import. (`#34 <https://github.com/ros-infrastructure/vcs2l/pull/34>`_)
* Added support for empty repository entries and improved validation output. (`#35 <https://github.com/ros-infrastructure/vcs2l/pull/35>`_)
* Add ruff to the pre-commit (`#27 <https://github.com/ros-infrastructure/vcs2l/pull/27>`_)
* 🛠️ Bump actions/checkout from 4.2.2 to 5.0.0 (`#31 <https://github.com/ros-infrastructure/vcs2l/pull/31>`_)
* 🛠️ Bump actions/setup-python from 5.5.0 to 5.6.0 (`#32 <https://github.com/ros-infrastructure/vcs2l/pull/32>`_)
* Add contribution templates (`#23 <https://github.com/ros-infrastructure/vcs2l/pull/23>`_)
* Restrict push workflow to main branch. (`#30 <https://github.com/ros-infrastructure/vcs2l/pull/30>`_)
* Add GitHub actions to the dependabot configuration. (`#28 <https://github.com/ros-infrastructure/vcs2l/pull/28>`_)
* Rename master branch reference to main in tests. (`#29 <https://github.com/ros-infrastructure/vcs2l/pull/29>`_)
* Contributors: Leander Stephen D'Souza, Stefan Hoffmann, Yuki Furuta.

1.1.2 (2025-08-02)
------------------
* Configuration updates for stdeb release to bootstrap repository. (`#25 <https://github.com/ros-infrastructure/vcs2l/pull/25>`_)

1.1.1 (2025-07-30)
------------------
* Changed base python version to 3.5. (`#21 <https://github.com/ros-infrastructure/vcs2l/pull/21>`_)
* Release 1.1.1 (`#22 <https://github.com/ros-infrastructure/vcs2l/pull/22>`_)

1.1.0 (2025-07-11)
------------------
* Fix GitHub workflow to pass on Ubuntu/Mac/Windows (`#2 <https://github.com/ros-infrastructure/vcs2l/pull/2>`_)
* Deprecate pkg_resources in favor of importlib.metadata (`#4 <https://github.com/ros-infrastructure/vcs2l/pull/4>`_)
* Updated documentation to point to the new vcs2l name. (`#12 <https://github.com/ros-infrastructure/vcs2l/pull/12>`_)
* Added ignores for pytest cache, bytecode, and virtual environments. (`#10 <https://github.com/ros-infrastructure/vcs2l/pull/10>`_)
* Added base pre-commit hooks for whitespaces and trailing newlines. (`#6 <https://github.com/ros-infrastructure/vcs2l/pull/6>`_)
* Add codespell as a pre-commit hook (`#11 <https://github.com/ros-infrastructure/vcs2l/pull/11>`_)
* Migrate python package to vcs2l (`#16 <https://github.com/ros-infrastructure/vcs2l/pull/16>`_)
* Add Python 3.5 support (`#19 <https://github.com/ros-infrastructure/vcs2l/pull/19>`_)
* Migrate tests to use ros-infrastructure links (`#17 <https://github.com/ros-infrastructure/vcs2l/pull/17>`_)
* Prep for release (`#13 <https://github.com/ros-infrastructure/vcs2l/pull/13>`_)
* Contributors: Leander Stephen D'Souza
