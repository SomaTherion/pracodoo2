from odoo import models, fields, api

class Empleados(models.Model):
    _name = 'agenda.empleados'
    dni = fields.Char('DNI', required=True)
    nombre = fields.Char('Nombre', required=True)
    apellidos = fields.Char('Apellidos', required=True)
    provincia = fields.Many2one('agenda.departamentos', 'Departamento')



    @api.one
    def limpiar(self):
        self.nombre = ""
        self.apellidos = ""
        return True

    @api.multi
    def limpia_todo(self):
        done_recs = self.search([('dni', '=', '0')])
        done_recs.write({'dni': '1'})
        return True

