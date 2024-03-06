from odoo import fields, models


class Ticket(models.Model):
    _name = 'todo.app.ticket'

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
    number = fields.Integer(string="Number")
    tag = fields.Char(string="Tag")
    state = fields.Selection([('new', 'New'), ('in_progress', 'In Progress'), ('done', 'Done')], string="State")
    file = fields.Binary(string="File")
