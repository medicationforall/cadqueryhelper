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

def __make_quarter(
        width:float, 
        height:float, 
        web_thickness:float, 
        flange_thickness:float, 
        join_distance:float
    ) -> cq.Workplane:
    sPnts = [
    ((height-flange_thickness)-1+.00001, (web_thickness/2)),
    ((height-flange_thickness)+.00001, (web_thickness/2)+join_distance)
    ]
    quarter = (
        cq.Workplane()
        .lineTo(0,(web_thickness/2))
        .lineTo((height-flange_thickness)-1,(web_thickness/2))
        .spline(sPnts, includeCurrent=True)
        .lineTo((height-flange_thickness), width)
        .lineTo(height, width)
        .lineTo(height, 0)
        .close()
    )
    return quarter


def i_beam(
        length:float = 30, 
        width:float = 10, 
        height:float = 10, 
        web_thickness:float = 1, 
        flange_thickness:float = 1, 
        join_distance:float = 2
    ) -> cq.Workplane:
    '''
    https://en.wikipedia.org/wiki/I-beam
    https://en.wikipedia.org/wiki/File:I-BeamCrossSection.svg
    '''
    half_height=height/2
    half_width=width/2

    quarter = __make_quarter(half_width, half_height, web_thickness, flange_thickness, join_distance)

    work = quarter.extrude(length).translate((0,0,-1*(length/2)))
    work2 = work.rotate((1,0,0),(0,0,0),180)
    mirror_x = work.union(work2)
    work3 = mirror_x.rotate((0,1,0),(0,0,0), 180)
    return mirror_x.union(work3).rotate((0,1,0),(0,0,0), 90)
