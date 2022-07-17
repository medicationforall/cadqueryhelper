import cadquery as cq

w = 10
d = 10
h = 10

part1 = cq.Workplane().box(2*w,2*d,h)
part2 = cq.Workplane().box(w,d,2*h)
#part3 = Workplane().box(w,d,3*h)

assembly = cq.Assembly()
#assembly.add(box, name="cone0")
#assembly.add(box, name="cone1")
assembly.add(part1, loc=cq.Location(cq.Vector(-w,0,h/2)))
assembly.add(part2, loc=cq.Location(cq.Vector(1.5*w,-.5*d,h/2)), color=cq.Color(0,0,1,0.5))
#.add(part3, loc=Location(Vector(-.5*w,-.5*d,2*h)), color=Color("red"))

comp = assembly.toCompound()