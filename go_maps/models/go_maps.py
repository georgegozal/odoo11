from odoo import fields, models , api, _
from odoo.exceptions import ValidationError



class GoMaps(models.Model):
    _name = 'go.maps'
    
    address_latitude = fields.Char(string='Building Latitude', size=128)
    address_longitude = fields.Char(string='Building Longitude', size=128)
    address_direction_link = fields.Char(string='Google Map Direction')#, compute='_generate_direction_link')

    #@api.one
    @api.onchange('address_latitude','address_longitude')
    #@api.depends('address_latitude','address_longitude')
    def _generate_direction_link(self):
        if self.address_latitude and self.address_longitude:
            #self.address_direction_link = 'maps://maps.google.com?saddr=Current+Location&daddr='+self.address_latitude+','+self.address_longitude
            self.address_direction_link = 'https://www.google.com/maps?saddr=My+Location&daddr='+self.address_latitude+','+self.address_longitude
        else:
            self.address_direction_link = ''

