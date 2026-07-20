import sympy as sp

x, y, z = sp.symbols("x y z")

P = (1 + x*y)**3*z + y**2*(1 + x*y)*(4 + 3*x*y)
Q = y + 3*x*(1 + x*y)**2*z + 3*x*y**2*(4 + 3*x*y)
R = 2*x - 3*x**2*y - x**3*z

F = sp.Matrix([P, Q, R])
det_jacobian = sp.factor(F.jacobian([x, y, z]).det())

points = [
    (sp.Rational(0), sp.Rational(0), sp.Rational(-1, 4)),
    (sp.Rational(1), sp.Rational(-3, 2), sp.Rational(13, 2)),
    (sp.Rational(-1), sp.Rational(3, 2), sp.Rational(13, 2)),
]

images = [
    tuple(sp.simplify(component.subs({x: a, y: b, z: c})) for component in F)
    for a, b, c in points
]

expected = (sp.Rational(-1, 4), sp.Rational(0), sp.Rational(0))

assert det_jacobian == -2
assert all(image == expected for image in images)

print("det(JF) =", det_jacobian)
for point, image in zip(points, images):
    print(f"F{point} = {image}")
print("All checks passed.")
