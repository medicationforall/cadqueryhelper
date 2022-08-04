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

def make_series(shape, size = 5, length_offset=None, width_offset=None, height_offset=None):
    series = cq.Assembly()
    length, width, height = __resolve_hit_box(shape)

    for i in range(size):
        print(f'loop iteration {length} {width} {height}')
        x_coord = 0
        y_coord = 0
        z_coord = 0

        if length_offset != None:
            x_coord = i * (length + length_offset)

        if width_offset != None:
            y_coord = i * (width + width_offset)

        if height_offset != None:
            z_coord = i * (height + height_offset)

        series.add(shape,  loc=cq.Location(cq.Vector(x_coord, y_coord, z_coord)))

    comp = series.toCompound()
    work = cq.Workplane("XZ").center(0, 0).workplane()
    work.add(comp)
    return work

def __resolve_hit_box(shape):
    attributes = dir(shape)
    if 'metadata' in attributes:
        meta = shape.metadata
        length = meta['length']
        width = meta['width']
        height = meta['height']
    else:
        raise Exception('Could not resolve shape metadata for series.')
    return length, width, height
