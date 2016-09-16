# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

# TODO: Clean this up and split it out into a seperate library.
# TODO: Add configuration.
# TODO: Detect if project is being built instead of served, and automatically
#       enable production mode.

import os

from lektor.pluginsystem import Plugin
from lektor.reporter import reporter
from lektor.utils import portable_popen

class BrunchSupportPlugin(Plugin):
    name = 'Brunch Support Plugin'
    description = 'Enables support for running a Brunch watcher.'

    def __init__(self, *args, **kwargs):
        Plugin.__init__(self, *args, **kwargs)
        self.brunch_process = None

    def is_production(self, build_flags):
        return bool(build_flags.get('production'))

    def run_brunch(self, build_flags, watch=False):
        brunch_root = os.path.join(self.env.root_path, 'brunch')
        args = [os.path.join(brunch_root, 'node_modules', '.bin', 'brunch')]
        if watch:
            args.append('watch')
        else:
            args.append('build')
        if self.is_production(build_flags):
            args.append('--production')
        return portable_popen(args, cwd=brunch_root)

    def npm_install(self):
        reporter.report_generic('Installing NPM dependencies')
        brunch_root = os.path.join(self.env.root_path, 'brunch')
        portable_popen(['npm', 'install'], cwd=brunch_root).wait()

    def on_server_spawn(self, build_flags, **extra):
        self.npm_install()
        reporter.report_generic('Spawning Brunch watcher')
        self.brunch_process = self.run_brunch(build_flags, watch=True)

    def on_server_stop(self, **extra):
        if self.brunch_process is not None:
            reporter.report_generic('Stopping Brunch watcher')
            self.brunch_process.kill()

    def on_before_build_all(self, builder, **extra):
        self.npm_install()
        reporter.report_generic('Starting Brunch build')
        self.run_brunch(builder.build_flags).wait()
        reporter.report_generic('Brunch build finished')
