class SinhVien:
    def __init__(self, _id, _name, _sex, _major, _diemTB):
        self._id = _id
        self._name = _name
        self._sex = _sex
        self._major = _major
        self._diemTB = _diemTB
        self._hocLuc = None  

    
    def __str__(self):
        return f"ID: {self._id}, Name: {self._name}, Sex: {self._sex}, Major: {self._major}, DiemTB: {self._diemTB}, HocLuc: {self._hocLuc}"

