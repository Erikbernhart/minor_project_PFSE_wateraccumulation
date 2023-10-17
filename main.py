from handcalcs.decorator import handcalc
import forallpeople as si

@handcalc()
def debit(area: float, n: float, ir=float) -> float:
    """
    calculates the debit of rainwater with the constant ir:5*10-5 from NEN1991-1-1-3 table NB 1
    area is in m^2, and n is the number of overloads per area.

    """
    ir=0.00005
    Qhi = (area * ir) / n
    return Qhi


@handcalc()
def waterheight(width_overload: float, Qhi: float) -> float:
    """
    calculates the waterheight above the overload 
    with the debit and overload width in mm.
    """
    Dndi=0.7 * ((Qhi / (width_overload/1000)) ** (2/3))*10**3
    return Dndi

@handcalc()
def water_above_roof(Dndi: float) -> float:
    dhw = Dndi + 30
    return dhw

@handcalc()
def critical_height(height_of_overload:float) -> float:
    Hcrit = height_of_overload - 30
    return Hcrit
