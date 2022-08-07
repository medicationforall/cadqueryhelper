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


def pipe():
    #https://github.com/CadQuery/cadquery/issues/1132
    pipe_path = cq.Workplane("XZ").spline([(0,0), (20,-20), (50,-20), (50,-30)])
    pipe = cq.Workplane("XY").circle(5).sweep(pipe_path, multisection=0, isFrenet=False, clean=False)

    meta = {'type':'pipe'}
    pipe.metadata = meta
    return pipe
