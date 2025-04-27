import cadquery as cq
from cadqueryhelper import HelperPlate

helper_bp = HelperPlate()
helper_bp.make()
helper_ex = helper_bp.build_assembly()

#show_object(helper_ex)
helper_ex.export("gltf/helper_ex.gltf")