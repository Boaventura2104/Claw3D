from pathlib import Path

path = Path("GROWTH_OFFICE.md")
text = path.read_text(encoding="utf-8")

new_section3 = """## 3. Backlog operacional vivo (24/03/2026)\n| Oportunidade / Cliente | Frente | Owner | Status | Próximo Passo | Dependência / Bloqueio | Sinal de Receita |\n| --- | --- | --- | --- | --- | --- | --- |\n| Portal Growth Automation (landing + portal Supabase para PJotaHub) | Captura | Sheldon | Briefing e ICP em andamento; stack Supabase + Claude Code + Codex definidos. | Finalizar ICP, confirmar stack com equipe técnica e agendar diagnóstico de 30 min. | Precisa da equipe escolher janelas e confirmar prazo de entrega. | Estimativa R$ 12k–18k (MVP landing e automações). |\n| Conversão automatizada (n8n + Claude + LLMs) | Conversão | Sheldon & Closer | Lead em qualificação; checklist ainda em construção, falta protótipo rápido. | Montar checklist, aplicar no lead e gerar protótipo curto para validar ROI. | Falta tempo técnico para protótipo antes da proposta final. | Proposta potencial de R$ 9k–12k por pacote de automações incrementais. |\n| Programa de retenção & vibecoding (cliente atual com metas de engajamento) | Expansão | Sheldon / Builder | Outcome review conduzido, upgrades mapeados e em validação com o cliente. | Roda de valor (40 min) + sugerir retainer de R$ 8k. | Depende da agenda do cliente e da capacidade do Builder. | Retainer mensal de R$ 8k + possíveis upsells. |\n| Growth Office Operating Review (estrutura do escritório) | Estratégia interna | Sheldon | Revisão em andamento; gaps estruturais identificados e documentados; GROWTH + HEARTBEAT + MEMORY precisam de sincronização. | Traduzir lacunas em ações (log, checklist, handoff, memória) e agendar o próximo heartbeat com ata. | Precisa de input do Closer e Builder para ordenar backlog vivo e confirmar prioridade. | Cockpit operacional maduro liberando próximos passos claros. |\n| Opportunity Ledger (board de captura + CRM leve) | Captura | Sheldon | Sem log central; leads continuam em notas soltas, pipeline perde ritmo. | Modelar board leve (Notion/Airtable/planilha) com origem, ICP, valor, urgência e próximo passo; migrar as oportunidades atuais. | Precisa decidir ferramenta e definir frequência de atualização. | Pipeline com origem, urgência e status visíveis para acelerar follow-up. |\n| Ritmo do Growth Office & Memória viva | Estratégia interna | Sheldon | Ritmo quinzenal definido, mas execuções nem sempre registradas; memória vive fora do cockpit. | Amarrar HEARTBEAT + GROWTH_OFFICE + MEMORY em checklist pré-revisão e definir guardião de ata para cada ciclo. | Depende da confirmação do Closer e Builder na cadência quinzenal. | Revisões com ata, backlog atualizado e decisões registradas na memória. |\n"""
start = text.index("## 3.")
end = text.index("## 4.")
text = text[:start] + new_section3 + "\n" + text[end:]

new_subsection_4_7 = """### 4.7. Opportunity ledger & backlog higiene\n- Manter colunas mínimas (origem, frente, ICP, valor, urgência, próximo passo, owner e dependências) para cada oportunidade do board.  \n- Atualizar o ledger antes de cada heartbeat e sincronizar essa linha com a Seção 3 para evitar duplicidade.  \n- Definir guardião da glicose (Sheldon) para verificar se o board está sendo usado e que os líderes atualizam com decisões, bloqueios e mudanças de status.\n\n"""
insert_4_7 = text.index("## 5.")
text = text[:insert_4_7] + new_subsection_4_7 + text[insert_4_7:]

new_section5 = """## 5. Memória e estrutura viva\n- O Growth Office agora documenta backlog, SOPs e riscos dentro deste arquivo, e o MEMORY.md acompanha com entradas datadas.  \n- O backlog da Seção 3 já inclui Opportunity Ledger e Growth Rhythm; atualizar o HEARTBEAT deve trazer links diretos para cada linha e o MEMORY precisa registrar o guardião da ata.  \n- HEARTBEAT continua sendo o checklist leve que conecta status atual a decisões e riscos.  \n- Antes de cada revisão, alinhar GROWTH_OFFICE + HEARTBEAT + MEMORY e assegurar que cada oportunidade tem owner, próxima ação e dependências claras.\n\n"""
start = text.index("## 5.")
end = text.index("## 6.")
text = text[:start] + new_section5 + text[end:]

new_section6 = """## 6. Pacotes de trabalho (MVP vs Fase 2)\n1. **MVP**: Atualizar a Seção 3 (incluindo Opportunity Ledger e Growth Rhythm), aplicar o checklist capture→conversion no lead mais quente e garantir que o board esteja visível ao Closer. *(Owner: Sheldon, prazo: 25/03/2026; condição: board de oportunidades criado e checklist aplicado).*  \n2. **Fase 2**: Estruturar o playbook Builder (handoff + cadência de entrega) e documentar o sprint de valor pós-entrega, alimentando o HEARTBEAT com checkpoints semanais. *(Owner: Sheldon + Builder, prazo: 30/03/2026).*  \n3. **Fase 3**: Embutir o ritual de HEARTBEAT + MEMORY + GROWTH, com ata quinzenal, guardião da cadência e integração automática do ledger. *(Owner: Sheldon, prazo: 31/03/2026; condição: cadência quinzenal oficializada).*\n\n"""
start = text.index("## 6.")
end = text.index("## 7.")
text = text[:start] + new_section6 + text[end:]

new_section7 = """## 7. Próximos passos e responsáveis\n- **Sheldon**: finalizar briefing do Portal Growth Automation, criar o Opportunity Ledger (board, template e cadência), aplicar o checklist capture→conversion e garantir que o HEARTBEAT + MEMORY entreguem ata antes da próxima revisão.  \n- **Closer**: aplicar checklist de conversão no lead n8n + Claude e registrar validação com Boaventura, entregando evidências até 24/03.  \n- **Builder/Ops**: preparar esboço de entrega para o retainer vibecoding, confirmar capacidade para o novo sprint e alimentar os checkpoints do HEARTBEAT até 27/03.  \n- **Todos**: revisar HEARTBEAT.md, a Seção 2, o Opportunity Ledger e a seção 3 antes do próximo encontro quinzenal; quem liderar a seção deve registrar ata simples com próximos passos.\n\n"""
start = text.index("## 7.")
end = text.index("## 8.")
text = text[:start] + new_section7 + text[end:]

new_section8 = """## 8. Riscos & decisões estratégicas\n- **Risco de pipeline**: a ausência de log central está empurrando oportunidades para notas individuais; sem um board, leads esfriam, e o Closer não consegue priorizar.  \n- **Risco de memória e cadência**: sem ata e registro automatizado, decisões e dependências se perdem e o heartbeat vira ruído.  \n- **Decisão**: tratar a Seção 3, o Opportunity Ledger, o HEARTBEAT e o MEMORY como a única fonte, atualizando tudo assim que uma linha mudar e garantindo guardião da ata por ciclo.\n"""
start = text.index("## 8.")
text = text[:start] + new_section8

path.write_text(text, encoding="utf-8")
