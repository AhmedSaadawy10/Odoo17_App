from odoo import models, fields, api, exceptions


class CustomerInherit(models.Model):
    _inherit = "res.partner"
    _name = "res.partner"

    related_patient_id = fields.Many2one("hms.patient")
    vat = fields.Char(required=True)

    # Add a constraint on CRM customer model which prevents
    # linking customer with email which already exists in
    # patient model.
    @api.constrains('email')
    def _check_duplicate_email(self):
        for partner in self:
            if partner.related_patient_id and partner.related_patient_id.email == partner.email:
                raise exceptions.ValidationError('Email already exists in the patient model.')

    # ➢ Prevent users to delete any customer linked to a patient
    def unlink(self):
        for rec in self:
            if rec.related_patient_id:
                raise exceptions.UserError("You cannot delete any customer linked to a patient")
        super.unlink()

