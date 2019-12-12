# -*- coding: utf-8 -*-
import random

from odoo import models, fields, api, tools


class player(models.Model):
    _name = 'game.player'
    name = fields.Char()
    planetes = fields.One2many('game.planets', 'player')
    probaKanban = fields.One2many(related='planetes')  # Per al kanban


class planets(models.Model):
    _name = 'game.planets'
    image = fields.Binary()
    # image_small = fields.Binary(string='Image', compute='_get_images', store=True)
    name = fields.Char()
    player = fields.Many2one('game.player')
    flota = fields.One2many('game.fleet', 'naves')
    resources = fields.One2many('game.resource', 'planetsR')
    minas = fields.One2many('game.mines', 'planetsM')
    recursosKanban = fields.One2many(related='resources')  # Per al kanban


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


class mina(models.Model):
    _name = 'game.mina'
    name = fields.Char()
    nivell = fields.Integer(default=1)
