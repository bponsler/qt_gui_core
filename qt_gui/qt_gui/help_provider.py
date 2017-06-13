# Copyright (c) 2011, Dirk Thomas, Dorian Scholz, TU Darmstadt
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#   * Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.
#   * Redistributions in binary form must reproduce the above
#     copyright notice, this list of conditions and the following
#     disclaimer in the documentation and/or other materials provided
#     with the distribution.
#   * Neither the name of the TU Darmstadt nor the names of its
#     contributors may be used to endorse or promote products derived
#     from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
import os
import subprocess
import webbrowser
import xml.dom.minidom as dom

from python_qt_binding.QtCore import QObject, Slot

from .ros_package_helper import get_package_path

import rospkg


class HelpProvider(QObject):

    """Handler for the help action in the title bar of dock widgets."""

    def __init__(self):
        super(HelpProvider, self).__init__()

    @Slot(object)
    def plugin_help_request(self, plugin_descriptor):
        rp = rospkg.RosPack()
        package_name = plugin_descriptor.attributes()['package_name']
        package_path = rp.get_path(package_name)
        try:
            url = self.__get_manifest_url(package_path, MANIFEST_FILE)
        except (InvalidManifest, IOError):
            return
        webbrowser.open(url)

    def __get_manifest_url(self, dirpath, manifest_name):
        type_ = 'package'

        filename = os.path.join(dirpath, manifest_name)
        if os.path.isfile(filename):
            with open(filename, 'r') as f:
                content = f.read()

                # Locate the package element
                try:
                    d = dom.parseString(content)
                except Exception as e:
                    raise Exception("[%s] invalid XML: %s" % (filename, e))
                nodes = [t for t in d.childNodes if t.nodeType == t.ELEMENT_NODE and t.tagName == type_]
                if len(nodes) != 1:
                    raise Exception("manifest [%s] must have a single '%s' element" % (filename, type_))

                # Find the url nodes
                url = [t for t in nodes[0].childNodes if t.nodeType == t.ELEMENT_NODE and t.tagName == "url"]
                if len(url) > 0:
                    # Select the first url
                    text = "".join([n.data for n in url[0].childNodes if n.nodeType == n.TEXT_NODE])
                    return text.strip()

        raise Exception("Unable to locate manifest url: %s" % filename)
