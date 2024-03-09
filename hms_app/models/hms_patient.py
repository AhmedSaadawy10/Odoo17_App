from odoo import fields, models, api
from dateutil.relativedelta import relativedelta


class HmsPatient(models.Model):
    _name = "hms.patient"
    _rec_name = "f_name"

    f_name = fields.Char(string="First Name", required=True)
    l_name = fields.Char(string="Last Name", required=True)
    email = fields.Char("Email")
    _sql_constraints = [
        ("Duplicate_Email", "UNIQUE(email)", "Email Already Exists"),
    ]
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
    age = fields.Integer("Age", compute='_compute_age')
    state = fields.Selection([
        ('undetermined', "Undetermined"),
        ('good', "Good"),
        ('fair', "Fair"),
        ('serious', "Serious")
    ], string="States", default="undetermined")
    department_id = fields.Many2one("hms.department")
    department_capacity = fields.Integer(related="department_id.capacity")
    doctors_ids = fields.Many2many("hms.doctor")
    history_ids = fields.One2many("patient.log.history", "patient_id")

    def action_undetermined(self):
        for rec in self:
            rec.state = 'undetermined'

    def action_good(self):
        for rec in self:
            rec.state = 'good'

    def action_fair(self):
        for rec in self:
            rec.state = 'fair'

    def action_serious(self):
        for rec in self:
            rec.state = 'serious'

    @api.depends("birthdate")
    def _compute_age(self):
        for rec in self:
            if rec.birthdate:
                rec.age = relativedelta(fields.Date.today(), rec.birthdate).years
            else:
                rec.age = False

    @api.onchange('age')
    def _on_change_age(self):
        if self.age and self.age < 30:
            self.pcr = True
            return {
                'warning': {
                    'title': 'Note',
                    'message': 'PCR has been checked',
                    'type': 'notification',
                },
            }
        else:
            self.pcr = False

    def action_add_history(self):
        action = self.env['ir.actions.actions']._for_xml_id('hms_app.history_wizard_action')
        action['context'] = {
            'default_patient_id': self.id,

        }
        return action
