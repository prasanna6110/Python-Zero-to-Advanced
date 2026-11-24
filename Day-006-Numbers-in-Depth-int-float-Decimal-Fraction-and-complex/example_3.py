# Day 006 · Numbers in Depth: int, float, Decimal, Fraction and complex — complex numbers: AC circuit phasors
# Run: python example_3.py

import cmath, math

V = 230 * cmath.exp(1j * 0)           # 230 V at 0°
Z = complex(10, 5)                    # R = 10 Ω, X_L = 5 Ω
I = V / Z
print(f"Impedance |Z| = {abs(Z):.2f} Ω at {math.degrees(cmath.phase(Z)):.2f}°")
print(f"Current   |I| = {abs(I):.2f} A at {math.degrees(cmath.phase(I)):.2f}°")
S = V * I.conjugate()
print(f"Real power P = {S.real:.1f} W, reactive Q = {S.imag:.1f} VAR, pf = {S.real / abs(S):.3f}")
print(cmath.sqrt(-16), (3 + 4j).real, (3 + 4j).imag, abs(3 + 4j))
