from xml.dom import ValidationErr
from odoo import api, fields, models
from odoo.exceptions import ValidationError
import uuid


class MozLearning(models.Model):
    _name = "linhafala.moz_learning"
    _description = "Formulário Moz Learning"
    _inherit = [
        'mail.thread',
        'mail.activity.mixin'
    ]

    moz_learning_id = fields.Char(
        string="ID Moz Learning", readonly=True, unique=True)

    persons_involved_moz_learning_line_ids = fields.One2many('linhafala.person_involved', 'moz_learning_id',
                                                             string="Pessoas envolvidas")

    moz_learning_complaint_details_line_ids = fields.One2many('linhafala.moz_learning_complaint_details', 'moz_learning_complaint__details_id',
                                                              string="Formulário de Detalhes do Moz Learning")

    vbg_line_ids = fields.One2many('linhafala.gender_based_violence', 'gender_based_violence_id',
                                   string="Formulário de VBG (Violência Baseada no Gênero)")
    
    moz_learning_referral_line_ids = fields.One2many('linhafala.moz_learning.referral', 'moz_learning_referral_id',
                                   string="Formulário de Encaminhamento")

    call_id = fields.Many2one(
        comodel_name='linhafala.chamada', string="Chamada")

    wants_to_be_annonymous = fields.Boolean(
        "Consetimento Informado", default=True)

    fullname = fields.Char(string="Nome Completo")

    birthd_date = fields.Datetime(
        string="Data de Nascimento", widget="datetime", date_format="%d/%m/%Y %H:%M:%S")

    gender = fields.Selection(
        string='Sexo',
        selection=[
            ("male", "Masculino"),
            ("female", "Feminino"),
        ],
        help="Sexo"
    )
    have_a_phone = fields.Selection(
        string='Tem telefone',
        selection=[
            ("Sim", "Sim"),
            ("Não", "Não"),
        ],
        help="Tem telefone"
    )

    contact = fields.Char(string="Contacto", widget="phone_raw",
                          size=13, min_length=9, default="+258")
    other_means_of_contact = fields.Char(string="Outro meio de Contacto")

    id_number = fields.Selection(
        string='Tipo de Identificação',
        selection=[
            ("BI", "BI"),
            ("NUIT", "NUIT"),
            ("Cartão de Eleitor", "Cartão de Eleitor"),
            ("Cedula pessoal", " Cedula pessoal"),
            ("Certidão de Nascimento", " Certidão de Nascimento"),
            ("Carta de condução", "Carta de condução"),
            ("Outro", "Outro"),
        ],
        help="Tipo de documento de identificação"
    )

    document_number = fields.Char(string="Numero do documento", widget="phone_raw",
                                  size=13)

    isVictim = fields.Boolean(
        "O Denunciante é Vítima ?", default=True)

    provincia = fields.Many2one(
        comodel_name='linhafala.provincia', string="Província")

    distrito = fields.Many2one(
        comodel_name='linhafala.distrito', string="Districto")

    administrative_post = fields.Char(string="Posto Administrativo")

    locality = fields.Char(string="Localidade")

    community = fields.Char(string="Comunidade/Bairro - Escola")

    complaint_eligibility = fields.Selection(
        string='Elegibilidade da Queixa',
        selection=[
            ("Procedente", "Procedente"),
            ("Não Procedente", "Não Procedente")
        ],
        help="Elegibilidade da Queixa"
    )

    complaint_related_to = fields.Selection(
        string='Esta é uma reclamação reclacionada a',
        selection=[
            ("Ambiental", "Ambiental"),
            ("Social", "Social"),
            ("Desempenho do Projecto", "Desempenho do Projecto")
        ],
        help="Esta é uma reclamação reclacionada a"
    )

    specify = fields.Selection(
        string='Especifique',
        selection=[
            ("VBG", "VBG"),
            ("Morte", "Morte"),
            ("Corrupção", "Corrupção"),
            ("Ambiental(Geral)", "Ambiental"),
            ("Social (Geral)", "Social (Geral)"),
            ("Acidente grave", "Acidente grave"),
            ("Poluição Sonora", "Poluição Sonora"),
            ("Poluição do Ambiente", "Poluição do Ambiente"),
            ("Desempenho do projecto (Geral)", "Desempenho do projecto (Geral)"),
        ],
        help="Especifique"
    )

    type_of_vbg = fields.Selection(
        string='Qual o tipo',
        selection=[
            ("Abuso Sexual", "Abuso Sexual"),
            ("Assédio Sexual", "Assédio Sexual"),
            ("Exploração Sexual", "Exploração Sexual"),
            ("Outras formas de VBG", "Outras formas de VBG"),
        ],
        help="Qual o tipo"
    )

    level_of_urgency = fields.Selection(
        string='Nivel de urgência',
        selection=[
            ("Alto", "Alto"),
            ("Baixo", "Baixo"),
            ("Moderado", "Moderado"),
            ("Substancial", "Substancial")
        ],
        help="Nivel de urgência"
    )

    date_of_occurrence = fields.Datetime(
        string="Data de Ocorrência", widget="datetime", date_format="%d/%m/%Y %H:%M:%S")

    complaint_reception_channel = fields.Selection(
        string='Canal de recepção da reclamação',
        selection=[
            ("Email", "Email"),
            ("Formulário/Caixa", "Formulário/Caixa"),
            ("Ponto Focal Escola", "Ponto Focal Escola"),
            ("Linha Fala Criança", "Linha Fala Criança"),
            ("Ponto Focal Central", "Ponto Focal Central"),
            ("Ponto Focal Distrital de Gênero/Salvaguardas",
             " Ponto Focal Distrital de Gênero/Salvaguardas"),
            ("Ponto Focal Provincial de Gênero/Salvaguardas",
             " Ponto Focal Provincial de Gênero/Salvaguardas"),
        ],
        help="Canal de recepção da reclamação"
    )

    focal_point_name = fields.Char(
        string="Nome do ponto focal que recebeu a reclamação (caso tenha sido recebida presencialmente)")

    focal_point_contact = fields.Char(string="Contacto do ponto focal que recebeu a reclamação", widget="phone_raw",
                                      size=13, min_length=9, default="+258")

    moz_learning_details = fields.Char(string="Resumo da queixa")

    date_of_receipt = fields.Datetime(
        string="Data de recepção", widget="datetime", date_format="%d/%m/%Y %H:%M:%S")

    attachment = fields.Char(string="Anexe aqui o seu documento ou fotografia")

    process_situation = fields.Selection(
        string='Situação do processo',
        selection=[
            ("Em curso", "Em curso"),
            ("Resolvido", "Resolvido")
        ],
        help="Situação do processo"
    )

    updated_at = fields.Datetime(string='Data de actualizaçäo',
                                 default=lambda self: fields.Datetime.now(), readonly=True)

    specify_others = fields.Char(string="Especifique Outros")

    created_by = fields.Many2one(
        'res.users', string='Criado por', default=lambda self: self.env.user, readonly=True)

    moz_learning_status = fields.Selection(
        string='Estado do caso',
        selection=[
            ("Aberto/Pendente", "Aberto/Pendente"),
            ("Dentro do sistema", "Dentro do sistema"),
            ("Assistido", "Assistido"),
            ("Encerrado", "Encerrado"),
        ],default="Aberto/Pendente",
        help="Estado do caso"
    )


    @api.model
    def save(self, vals):
        return super(MozLearning, self).write(vals)
    
    @api.model
    def edit(self, vals):
        return super(MozLearning, self).write(vals)


class MozLearningReferral(models.Model):
    _name = "linhafala.moz_learning.referral"
    _description = "Instituição de encaminhamento de moz learning"

    moz_learning_referral_id = fields.Integer(
        string="Instituição de encaminhamento de moz learning ID", readonly=True, unique=True)

    moz_learning_id = fields.Many2one(
        comodel_name='linhafala.moz_learning', string="Moz Learning")
    
    area_type = fields.Selection(
        string='Área de Encaminhamento',
        selection=[
            ("Institucional", "Institucional"),
            ("Não Institucional", "Não Institucional"),
        ],
        help="Área de Encaminhamento"
    )
    reference_area = fields.Many2one(
        comodel_name='linhafala.caso.referencearea', 
        string="Área de Referência",
        domain="[('area_type', '=', area_type)]"
    )
    reference_entity = fields.Many2one(
        comodel_name='linhafala.caso.referenceentity', string="Entidade de Referência")

    case_reference = fields.Many2one(
        comodel_name='linhafala.caso.casereference', 
        string="Pessoa de Contacto",
        domain="[('reference_entity', '=', reference_entity)]"
        )
    
    spokes_person_phone = fields.Char(
        string="Telefone do Responsável", related='case_reference.contact')
    provincia = fields.Many2one(
        comodel_name='linhafala.provincia', string="Provincia")
    distrito = fields.Many2one(
        comodel_name='linhafala.distrito', string="Districto")

    moz_learning_status = fields.Selection(
        string='Estado do caso',
        selection=[
            ("Aberto/Pendente", "Aberto/Pendente"),
            ("Dentro do sistema", "Dentro do sistema"),
            ("Assistido", "Assistido"),
            ("No Arquivo Morto", "No Arquivo Morto"),
            ("Encerrado", "Encerrado")
        ],default="Aberto/Pendente",
        help="Estado do caso"
    )

    @api.onchange('provincia')
    def _provincia_onchange(self):
        for rec in self:
            return {'value': {'distrito': False}, 'domain': {'distrito': [('provincia', '=', rec.provincia.id)]}}

    @api.onchange('reference_area')
    def _reference_area_onchange(self):
        for rec in self:
            return {'value': {'reference_entity': False}, 'domain': {'reference_entity': [('reference_area', '=', rec.reference_area.id)]}}

    @api.constrains('assistance_status')
    def _check_assistance_status(self):
        for record in self:
            if record.assistance_status != 'Aberto/Pendente' and record.assistance_status != 'Dentro do sistema' and record.assistance_status != 'Assistido' and record.assistance_status != 'Encerrado':
                raise ValidationError(
                    "Por favor, selecione o estado do caso para prosseguir.")

    @api.constrains('moz_learning_status')
    def _check_moz_learning_status(self):
        for record in self:
            if record.moz_learning_status != 'Aberto/Pendente' and record.moz_learning_status != 'Dentro do sistema' and record.moz_learning_status != 'Assistido' and record.moz_learning_status != 'Encerrado':
                raise ValidationError(
                    "Por favor, selecione o estado do caso para prosseguir.")
