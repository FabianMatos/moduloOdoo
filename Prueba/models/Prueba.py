# -*- coding: utf-8 -*- 
# Part of Odoo. See LICENSE file for full copyright and licensing details. 
from odoo import api, fields, models 
from datetime import datetime 

class Prueba(models.Model): 
    _name = 'ej.Prueba' 
    Nombre = fields.Char(string='Nombre', required=True) 
 
    Edad = fields.Integer(string='Edad', required=True) 
 
