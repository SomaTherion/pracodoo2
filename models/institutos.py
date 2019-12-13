
from odoo import models, fields, api

class Empresas(models.Model):Instituto
    _name = 'agenda.institutos'
    cod = fields.Char('cod', required=True)
    nombre = fields.Char('Nombre del instituto', required=True)


    def name_get(self):
        res=[]
        for record in self:
            name = record.nombre
            res.append((record.id, name))
        return res



