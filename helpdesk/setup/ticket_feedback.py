import frappe

OPTIONS = {
	0.2: ["A resposta não ajudou", "Não resolveu meu problema"],
	0.4: ["Atraso no tempo de resposta", "Resposta adequada, mas lenta"],
	0.6: ["Resposta clara e objetiva", "Respostas de grande ajuda, porém com alguma espera"],
	0.8: ["Soluções rápidas e precisas", "Suporte ágil e informativo"],
	1.0: ["Experiencia de suporte excepcional", "Ajuda instantânea e de alto nível"],
}


def create_ticket_feedback_options():
	for rating in OPTIONS:
		for label in OPTIONS[rating]:
			doc = {
				"doctype": "HD Ticket Feedback Option",
				"rating": rating,
				"label": label,
			}
			if not frappe.db.exists(doc):
				frappe.get_doc(doc).insert()
