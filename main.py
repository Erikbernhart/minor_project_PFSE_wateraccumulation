from handcalcs.decorator import handcalc
import forallpeople as si

@handcalc()
def debit(area: float, n: float, I_r=float) -> float:
    """
    calculates the debit of rainwater with the constant I_r:5*10-5 from NEN1991-1-1-3 table NB 1
    area is in m^2, and n is the number of overloads per area.

    """
    I_r=0.00005
    Q_hi = (area * I_r) / n
    return Q_hi


@handcalc()
def waterheight(width_overload: float, Q_hi: float) -> float:
    """
    calculates the waterheight above the overload 
    with the debit and overload width in mm.
    """
    D_ndi=0.7 * ((Q_hi / (width_overload/1000)) ** (2/3))*10**3
    return D_ndi

@handcalc()
def water_above_roof(D_ndi: float, h_nd:float) -> float:
    d_hw = D_ndi + h_nd
    return d_hw

@handcalc()
def critical_height(h_nd:float,height_of_overload:float) -> float:
    Hcrit = h_nd+height_of_overload - 30
    return Hcrit
