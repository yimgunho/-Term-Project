class DataClass:
    def __init__(self):
        self.sum_de = None
        self.distrct_div_nm = None
        self.medcare_inst_nm = None
        self.emgncy_center_telno = None
        self.refine_lotno_addr = None
        self.refine_roadnm_addr = None
        self.refine_wgs84_logt = None
        self.refine_wgs84_lat = None

    def out_sum_de(self):
        return self.sum_de

    def out_distrct_div_nm(self):
        return self.distrct_div_nm

    def out_medcare_inst_nm(self):
        return self.medcare_inst_nm

    def out_emgncy_center_telno (self):
        return self.emgncy_center_telno

    def out_refine_lotno_addr(self):
        return self.refine_lotno_addr

    def out_refine_roadnm_addr(self):
        return self.refine_roadnm_addr

    def out_refine_wgs84_logt(self):
        return float(self.refine_wgs84_logt)

    def out_refine_wgs84_lat(self):
        return float(self.refine_wgs84_lat)

    def in_sum_de(self, data):
        self.sum_de = data

    def in_distrct_div_nm(self, data):
        self.distrct_div_nm = data

    def in_medcare_inst_nm(self, data):
        self.medcare_inst_nm = data

    def in_emgncy_center_telno(self, data):
        self.emgncy_center_telno = data

    def in_refine_lotno_addr(self, data):
        self.refine_lotno_addr = data

    def in_refine_roadnm_addr(self, data):
        self.refine_roadnm_addr = data

    def in_refine_wgs84_logt(self, data):
        self.refine_wgs84_logt = data

    def in_refine_wgs84_lat(self, data):
        self.refine_wgs84_lat = data

