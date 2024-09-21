from rolepermissions.roles import AbstractUserRole


class Admin(AbstractUserRole):
    available_permissions = {'create_music': True, 'get_music':True, 'update_music': True, 'delete_music': True}


class StaffI(AbstractUserRole):
    available_permissions = {'create_music': True, 'get_music':True, 'update_music': True, 'delete_music': True}


class Regent(AbstractUserRole):
    available_permissions = {'create_music': True, 'get_music':True, 'update_music': True}

class Component(AbstractUserRole):
    available_permissions = {'get_music':True}

