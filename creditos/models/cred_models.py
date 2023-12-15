from odoo import models, fields, api

class CreditOperation(models.Model):
    _name = 'credit.credit_operation'
    _description = 'Credit Operations'

    name = fields.Char(string='Name', required=True)
    amount = fields.Float(string='Amount')
    interest_rate = fields.Float(string='Interest Rate')
    duration = fields.Integer(string='Duration (months)')
    amortization_ids = fields.One2many('credit.amortization', 'credit_operation_id', string='Amortization Schedule')
    account_statement_ids = fields.One2many('cuenta.account_statement', 'credit_operation_id', string='Account Statements')

    def generate_amortization_schedule(self):
        for operation in self:
            # Lógica de cálculo de amortización (puede variar según tus necesidades específicas)
            amortization_vals = []
            for installment_number in range(1, operation.duration + 1):
                # Cálculos de amortización aquí (principal, interés, total)
                amortization_vals.append({
                    'installment_number': installment_number,
                    # Otros campos de amortización
                })
            operation.write({'amortization_ids': [(0, 0, vals) for vals in amortization_vals]})

    def generate_account_statement(self):
        for operation in self:
            # Lógica de generación de estados de cuenta (puede variar según tus necesidades específicas)
            statement_vals = []
            # Cálculos de apertura, cierre, transacciones, etc.
            operation.write({'account_statement_ids': [(0, 0, vals) for vals in statement_vals]})
#--------------------------------------------------------------------------

class AmortizationTable(models.Model):
    _name = 'credit.amortization'
    _description = 'Amortization Table'

    credit_operation_id = fields.Many2one('credit.credit_operation', string='Credit Operation')
    payment_date = fields.Date(string='Payment Date')
    installment_number = fields.Integer(string='Installment Number')
    principal_amount = fields.Float(string='Principal Amount')
    interest_amount = fields.Float(string='Interest Amount')
    total_amount = fields.Float(string='Total Amount')

class AccountStatement(models.Model):
    _name = 'cuenta.account_statement'
    _description = 'Account Statement'

    credit_operation_id = fields.Many2one('credit.credit_operation', string='Credit Operation')
    statement_date = fields.Date(string='Statement Date')
    opening_balance = fields.Float(string='Opening Balance')
    closing_balance = fields.Float(string='Closing Balance')
    transactions = fields.One2many('cuenta.account_transaction', 'account_statement_id', string='Transactions')

class AccountTransaction(models.Model):
    _name = 'cuenta.account_transaction'
    _description = 'Account Transaction'

    account_statement_id = fields.Many2one('cuenta.account_statement', string='Account Statement')
    transaction_date = fields.Date(string='Transaction Date')
    description = fields.Char(string='Description')
    amount = fields.Float(string='Amount')

#---------------------------------------------------------------------