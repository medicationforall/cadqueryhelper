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


def cylinder(radius = 2.5, height = 5 ):
    #cylinder = cq.Workplane().circle(diameter).extrude(height)
    work = cq.Workplane().cylinder(height, radius)

    meta = {'type':'cylinder', 'radius':radius, 'height':height, 'length':radius*2, 'width':radius*2}
    work.metadata = meta
    return work
