# -*- coding: utf-8 -*-
from odoo import http


class Creditos(http.Controller):
    @http.route('/creditos/creditos', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/creditos/creditos/objects', auth='public')
    def list(self, **kw):
        return http.request.render('creditos.listing', {
            'root': '/creditos/creditos',
            'objects': http.request.env['creditos.creditos'].search([]),
        })

    @http.route('/creditos/creditos/objects/<model("creditos.creditos"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('creditos.object', {
            'object': obj
        })
