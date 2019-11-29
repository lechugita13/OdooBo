# -*- coding: utf-8 -*-

from odoo import models, fields, api


class player(models.Model):
    _name = 'game.player'
    name = fields.Char()
    planetes = fields.One2many('game.planets', 'player')


class planets(models.Model):
    _name = 'game.planets'
    name = fields.Char()
    player = fields.Many2one('game.player')
    flota = fields.One2many('game.fleet', 'naves')
    image = fields.Binary()
    recursos1 = fields.One2many('game.recurso', 'recursos')


class fleet(models.Model):
    _name = 'game.fleet'
    name = fields.Char()
    naves = fields.Many2one('game.planets')


class recursos(models.Model):
    _name = 'game.recursos'
    name = fields.Char()
    cantidad = fields.Float()
    recurso = fields.Many2one('game.recurs')
    recursPlanetes = fields.Many2one('game.planetes')


class recurs(models.Model):
    _name = 'game.recurs'
    name = fields.Char()
    image = fields.Binary()
