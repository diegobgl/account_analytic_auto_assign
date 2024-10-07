from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    def assign_analytic_account_to_lines(self):
        """
        Este método verifica que si la cabecera de un asiento contable tiene una cuenta analítica
        pero las líneas no, entonces asigna la cuenta analítica de la cabecera a las líneas.
        """
        for move in self:
            if move.analytic_account_id:
                # Obtener las líneas que no tienen cuenta analítica asignada
                lines_without_analytic = move.line_ids.filtered(lambda line: not line.analytic_account_id)
                
                # Asignar la cuenta analítica de la cabecera a las líneas que no la tengan
                if lines_without_analytic:
                    lines_without_analytic.write({
                        'analytic_account_id': move.analytic_account_id.id
                    })

    def action_assign_analytic_account(self):
        """
        Acción invocable desde el tree view para asignar cuentas analíticas a las líneas
        en función de la cuenta de la cabecera.
        """
        self.assign_analytic_account_to_lines()
