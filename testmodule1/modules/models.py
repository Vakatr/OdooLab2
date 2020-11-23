from odoo import api, fields, models

class NewModule(models.Model):
_name = 'feedback.form'
_rec_name = 'name'
_description = 'New Description'

name = fields.Char()