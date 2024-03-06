from odoo import fields, models


class Doctor(models.Model):
    _name = "hms.doctor"
    _rec_name = "l_name"

    f_name = fields.Char(string="First Name")
    l_name = fields.Char(string="Last Name")
    image = fields.Binary()
