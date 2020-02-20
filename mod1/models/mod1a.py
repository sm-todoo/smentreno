# -*- coding: utf-8 -*-

from odoo import models, fields, api


class mod1a(models.Model):
     _name = 'mod1a.mod1a'
     _description = 'mod1a.mod1a'

     nombre = fields.Char()
     valor = fields.Integer()
     valor2 = fields.Float(compute="_value_pc", store=True)
     descripcion = fields.Text()

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
