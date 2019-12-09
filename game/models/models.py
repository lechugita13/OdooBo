# -*- coding: utf-8 -*-
import random

from odoo import models, fields, api, tools


class player(models.Model):
    _name = 'game.player'
    name = fields.Char()
    planetes = fields.One2many('game.planets', 'player')
    probaKanban = fields.One2many(related='planetes')  # Per al kanban



    @api.multi
    def createPlanet(self):
        for p in self:
            f_template = self.env.ref('game.planets1')
            names = ["Ardglass", "Abingdon", "Swindlincote", "Rotherham", "Far Water", "Todmorden", "Walden",
                     "Lanercoast", "Aempleforth", "Barkamsted", "Swindmore", "Mountmend", "Dalmellington",
                     "Blencogo", "Beggar's Hole", "Faversham", "Lindow", "Dungannon", "Doveport", "Peterbrugh",
                     "Limesvilles",
                     "Grimsby", "Thralkeld", "Dawsbury", "Rotherhithe", "Pavv", "Holmfirth", "Dalmellington",
                     "Eastcliff", "Bleakburn"]
            f = self.env['game.planets'].create({
                'name': str(random.choice(names)),
                'image': f_template.image,
                'player': p.id
            })



class planets(models.Model):
    _name = 'game.planets'
    image = fields.Binary()
    image_small = fields.Binary(string='Image', compute='_get_images', store=True)
    name = fields.Char()
    player = fields.Many2one('game.player')
    flota = fields.One2many('game.fleet', 'naves')
    resources = fields.One2many('game.resource', 'planetsR')



    @api.depends('image')
    def _get_images(self):
        for i in self:
            image = i.image
            data = tools.image_get_resized_images(image)
            i.image_small = data["image_small"]




class fleet(models.Model):
    _name = 'game.fleet'
    name = fields.Char()
    naves = fields.Many2one('game.planets')


class resource(models.Model):
    _name = 'game.resource'
    name = fields.Char()
    image = fields.Binary()
    cantidad = fields.Float()
    planetsR = fields.Many2one('game.planets')

    # recurso = fields.Many2one('game.recurs')
