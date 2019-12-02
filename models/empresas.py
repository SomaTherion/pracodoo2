
from odoo import models, fields, api

class Empresas(models.Model):
    _name = 'agenda.empresas'
    cod = fields.Char('cod', required=True)
    nombre = fields.Char('Nombre de la empresa', required=True)


    def name_get(self):
        res=[]
        for record in self:
            name = record.nombre
            res.append((record.id, name))
        return res



