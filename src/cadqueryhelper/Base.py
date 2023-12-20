# Copyright 2023 James Adams
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


class Base:
    def __init__(self):
        self.make_called = False
        self.parent = None

    # make the class "with" compatible
    def __enter__(self):
            return self
    
    def __exit__(self, exc_type, exc_value, traceback):
         # overwite and add your own close logic
         pass

    def make(self, parent=None):
        self.parent = parent
        self.make_called = True

    def build(self):
        if self.make_called == False:
            raise Exception('Make has not been called')