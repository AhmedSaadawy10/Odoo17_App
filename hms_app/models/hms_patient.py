from odoo import fields, models


class HmsPatient(models.Model):
    _name = "hms.patient"
    _rec_name = "f_name"

    f_name = fields.Char(string="First Name", required=True)
    l_name = fields.Char(string="Last Name", required=True)
    email = fields.Char("Email")
    birthdate = fields.Date("Birthdate")
    history = fields.Html("History")
    blood_type = fields.Selection([
        ('a', 'Blood Type A'),
        ('b', 'Blood Type B'),
        ('ab', 'Blood Type AB'),
        ('o', 'Blood Type O'),
    ], string='Blood Type')
    pcr = fields.Boolean("Bcr")
    cr_ratio = fields.Float("CR Ratio")
    image = fields.Image("Image")
    ray = fields.Binary("Ray")
    address = fields.Text("Address")
    age = fields.Integer("Age")
    state = fields.Selection([
        ('undetermined', "Undetermined"),
        ('good', "Good"),
        ('fair', "Fair"),
        ('serious', "Serious")
    ], string="States")
    department_id = fields.Many2one("hms.department")
    department_capacity = fields.Integer(related="department_id.capacity")
    doctors_ids = fields.Many2many("hms.doctor")

