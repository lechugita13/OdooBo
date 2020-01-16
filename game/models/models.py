# -*- coding: utf-8 -*-
import random

from odoo import models, fields, api, tools
from openerp.exceptions import ValidationError


class player(models.Model):
    _name = 'game.player'
    name = fields.Char()
    planetes = fields.One2many('game.planets', 'player')

    @api.constrains('planetes')
    def _check_something(self):
        for r in self:
            if r.planetes > 10:
                raise ValidationError("You have too many planets %s" % r.planetes)

    @api.multi
    def create_new_planet(self):

        self.planetes.create({
            'planetes': self.id
        })


class planets(models.Model):
    _name = 'game.planets'
    image = fields.Binary()
    # image_small = fields.Binary(string='Image', compute='_get_images', store=True)
    name = fields.Char()
    player = fields.Many2one('game.player', ondelete='cascade')
    flota = fields.One2many('game.fleet', 'naves')
    resources = fields.One2many('game.resource', 'planetsR')
    minas = fields.One2many('game.mines', 'planetsM')
    recursosKanban = fields.One2many(related='resources')  # Per al kanban
    date_action = fields.Datetime('Date current action', required=False, readonly=True, select=True,
                                  default=lambda self: fields.datetime.now())


class fleet(models.Model):
    _name = 'game.fleet'
    name = fields.Char()
    naves = fields.Many2one('game.planets')


class resource(models.Model):
    _name = 'game.resource'
    name = fields.Char()
    cantidad = fields.Float()
    planetsR = fields.Many2one('game.planets')
    recurso = fields.Many2one('game.recurs')


class recurs(models.Model):
    _name = 'game.recurs'
    name = fields.Char()
    image = fields.Binary()


class mines(models.Model):
    _name = 'game.mines'
    name = fields.Char()
    coste = fields.Float()
    planetsM = fields.Many2one('game.planets')
    mine = fields.Many2one('game.mina')
    producio = fields.Float()

    @api.multi
    def produccio(self):
        for record in self:
            for minaEspe in record.mine:
                print(minaEspe)
                record.producio = float(record * record.producio)


class mina(models.Model):
    _name = 'game.mina'
    name = fields.Char()
    nivell = fields.Integer(default=1)
