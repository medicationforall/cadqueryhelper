# Copyright 2022 James Adams
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

import cadquery as cq

#@deprecated
def cube(
        length:float = 5, 
        width:float = 5, 
        height:float = 5 
    ) -> cq.Workplane:
    print('Deprecated use cq.Workplane("XY").box(length, width, height) instead')
    work = cq.Workplane("XY").box(length, width, height)
    return work
