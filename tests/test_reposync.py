# Copyright (C) 2014 Red Hat, Inc.
#
# This copyrighted material is made available to anyone wishing to use,
# modify, copy, or redistribute it subject to the terms and conditions of
# the GNU General Public License v.2, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY expressed or implied, including the implied warranties of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
# Public License for more details.  You should have received a copy of the
# GNU General Public License along with this program; if not, write to the
# Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.  Any Red Hat trademarks that are incorporated in the
# source code or documentation are not subject to the GNU General Public
# License and may only be used or replicated with the express permission of
# Red Hat, Inc.
#

from __future__ import absolute_import
from __future__ import unicode_literals
from tests import support
import reposync

class TestReposyncFunctions(support.TestCase):
    def test_parse_args(self):
        args = '-p /become/legend --repoid=silver --repoid=screen'.split()
        opts = reposync._parse_args(args)
        self.assertEqual(opts.repoid, ['silver', 'screen'])
        self.assertEqual(opts.download_path, '/become/legend')

    def test_pkgdir(self):
        self.assertEqual(reposync._pkgdir('/honey/../pie', 'crazy'),
                         '/pie/crazy')
