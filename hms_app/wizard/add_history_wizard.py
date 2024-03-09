from odoo import fields, models


class PatientLogHistory(models.TransientModel):
    _name = 'patient.log.history'
    _description = 'Add History Wizard'

    patient_id = fields.Many2one('hms.patient')
    current_date = fields.Datetime(related="patient_id.create_date")
    description = fields.Text()

    def action_add_history(self):
        pass


