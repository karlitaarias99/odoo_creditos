from odoo import http
from odoo.http import request

class CreditOperationController(http.Controller):

    @http.route('/credit_operations/amortization_table/<int:credit_operation_id>', auth='user', type='http')
    def show_amortization_table(self, credit_operation_id, **kw):
        credit_operation = request.env['credit.credit_operation'].browse(credit_operation_id)
        return request.render('creditos.listing', {'credit_operation': credit_operation})

    @http.route('/credit_operations/account_statement/<int:credit_operation_id>', auth='user', type='http')
    def show_account_statement(self, credit_operation_id, **kw):
        credit_operation = request.env['credit.credit_operation'].browse(credit_operation_id)
        return request.render('creditos.object', {'credit_operation': credit_operation})