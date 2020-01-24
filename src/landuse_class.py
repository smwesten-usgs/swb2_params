class landuse_parameter:

    def __init__(self, lu_code, lu_description):
        self.code = lu_code
        self.description = lu_description

    def set_curve_number(cn_a):
    """
    Given as equations 11a through 11d in Hawkins, R.H., Ward, T.J., Woodward, D.E.,
    and Van Mullem, J.A., 2009, Curve number hydrology: American Society of Civil Engineers, 106 p.

    """
        self.curve_num_a = cn_a
        self.curve_num_b = 37.8 + 0.622 * cn_a
        self.curve_num_c = 58.9 + 0.411 * cn_a
        self.curve_num_d = 67.2 + 0.328 * cn_a

    def set_rooting_depth(rz_a):
        self.rz_a = rz_a
        self.rz_b = rz_a * 0.95   # assume that rooting depths generally decrease slightly on a continuum from sand => silt => clay
        self.rz_c = rz_b * 0.95
        self.rz_d = rz_c * 0.95
