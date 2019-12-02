from odoo import models, fields, api

class Departamentos(models.Model):
    _name = 'agenda.departamentos'
    cod = fields.Char('cod', required=True)
    nombre = fields.Char('Nombre', required=True)
    empresa = fields.Many2one('agenda.empresas', 'Empresa')


    def name_get(self):
        res=[]
        for record in self:
            name = record.nombre
            res.append((record.id, name))
        return res

