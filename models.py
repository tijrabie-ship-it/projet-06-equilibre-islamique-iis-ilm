# models.py

def calculate_iis_ilm_equilibrium(alpha, psi, I0, C0, Z, D, beta, d, phi0, M_OF):
    """
    حساب التوازن الماكرو-اقتصادي (IIS-ILM) في سياق إسلامي.
    يعيد الدخل القومي (R*) ومعدل الربح المتوقع (rp*).
    """
    try:
        # حساب المتغير المستقل (Chi) لمعادلة سوق السلع
        chi = I0 + (4 * C0) + (2 * (1 - alpha) * (Z + D)) - (psi * Z)
        
        # معادلة منحنى IIS: rp = ((1 - 4*alpha) / psi) * R - (chi / psi)
        slope_iis = (1 - (4 * alpha)) / psi
        intercept_iis = -chi / psi
        
        # معادلة منحنى ILM: rp = (beta / d) * R + (phi0 + d*Z - M_OF) / d
        slope_ilm = beta / d
        intercept_ilm = (phi0 + (d * Z) - M_OF) / d
        
        # حساب نقطة التقاطع (R*, rp*)
        r_star = (intercept_ilm - intercept_iis) / (slope_iis - slope_ilm)
        rp_star = (slope_iis * r_star) + intercept_iis
        
        return {
            "success": True,
            "r_star": round(r_star, 2),
            "rp_star": round(rp_star, 2),
            "slope_iis": slope_iis,
            "intercept_iis": intercept_iis,
            "slope_ilm": slope_ilm,
            "intercept_ilm": intercept_ilm
        }
    except Exception as e:
        return {"success": False, "error": str(e)}