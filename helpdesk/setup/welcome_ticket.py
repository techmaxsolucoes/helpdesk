import frappe
from frappe.desk.form.assign_to import add as add_assign

AUTHOR_EMAIl = "mmorais@techmaxsolucoes.com.br"
AUTHOR_NAME = "Maxwell Morais"
CONTENT = """
<p>
Olá 👋
<br><br>
Eu estou extremamente feliz em saber que você decidiu testar o nosso sistema de suporte!
Nós estamos trabalhando para construir maneira para que equipes possam se comunicar e 
atender os clientes de forma bem otimizada.
<br><br>
Você pode começar agora mesmo configurando um email de suporte! Isso vai te ajudar a ver
como o seu suporte vai melhorar com o nosso sistema.
<br><br>
Se você encontrar algum problema, por favor nos envie um email para: 
<a href="mailto:suporte@techmaxsolucoes.com.br">suporte@techmaxsolucoes.com.br</a>
<br><br>
Boa sorte na sua jornada de melhoria do atendimento ao cliente,
qualquer dúvida, você sabe que pode contar conosco!
<br>
Maxwell Morais | TechMax Soluções.
"""


def create_welcome_ticket():
	create_contact()
	create_ticket()


def create_ticket():
	if frappe.db.count("HD Ticket"):
		return

	d = frappe.new_doc("HD Ticket")
	d.subject = "Bem vindo ao Helpdesk"
	d.description = CONTENT
	d.raised_by = AUTHOR_EMAIl
	d.contact = AUTHOR_NAME
	d.via_customer_portal = True
	d.insert()
	d.create_communication_via_contact(d.description)
	add_assign(
		{
			"doctype": "HD Ticket",
			"name": d.name,
			"assign_to": ["Administrator"],
		}
	)


def create_contact():
	frappe.get_doc(
		{
			"doctype": "Contact",
			"first_name": AUTHOR_NAME,
			"email_ids": [{"email_id": AUTHOR_EMAIl, "is_primary": 1}],
		}
	).insert()
