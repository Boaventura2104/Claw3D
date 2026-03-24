# Sheldon Growth Office Operating Review

## 1. Executive pulse
- Estamos operando em modo fundador-operacional total: cada movimento precisa gerar pipeline, avanço na conversão, entrega previsível ou expansão sistemática.  
- Revisão do escritório em 24/03/2026: mapeei gaps de estrutura, processos, memória e handoffs para que o Growth Office tenha um cockpit vivo antes da próxima HEARTBEAT.  
- Esta página agora é a fonte única para backlog, SOPs, riscos e decisões estratégicas; o objetivo imediato é fazer do GROWTH_OFFICE + HEARTBEAT + MEMORY uma trilogia sincronizada com o Opportunity Ledger como coluna vertebral.  

## 2. Frente por frente
| Frente | Estado atual (baseline) | Gap principal | Dono atual | Próximo avanço | Sinal de sucesso |
| --- | --- | --- | --- | --- | --- |
| Captura | Três oportunidades estão vivas aqui, mas não há log central replicável; o pipeline fica preso em notas soltas. | Falta um CRM leve (Notion/Airtable/planilha) que registre origem, ICP, valor e urgência em um Opportunity Ledger. | Sheldon | Modelar o leaderboard e migrar as três oportunidades do backlog com ICP + valor antes da próxima revisita. | Backlog com origem, valor, próximos passos e responsáveis visíveis fora da cabeça. |
| Conversão | Leads estão esquentando, mas a qualificação e a passagem para Builder continuam manuais. | Não existe checklist repetível para ROI, stakeholders decisores, urgência e investimento. | Sheldon + Closer | Formalizar checklist de decisão, aplicar no lead n8n + Claude e registrar os aprendizados no documento. | Checklist preenchido, lead pronto para proposta e sinal verde interno. |
| Entrega | O Builder tem informação, mas não há canal único para status, riscos e checkpoints; decisões ficam fora do cockpit. | Handoff informal, sem critérios de sucesso, datas ou canais de acompanhamento. | Builder / Ops | Documentar entrega corrente (Portal Growth Automation) com critérios, datas, riscos e checkpoints; compartilhar com Builder e Ops. | Owner com datas e checkpoints alinhados, Builder comprometido e riscos conhecidos. |
| Expansão | Upsell segue invisível; não há sprint regular de valor pós-entrega nem cadência com clientes. | Ausência de playbook pós-entrega para capturar oportunidades de expansão e retenção. | Sheldon | Criar playbook "Sprint de valor pós-entrega" e mapear dois clientes prioritários para retainer/upsell. | Lista de ações de expansão com metas mensais e responsáveis definidos. |
| Estratégia interna | Revisões de prioridades ocorrem em momentos isolados com pouca memória registrada. | Falta cadência quinzenal com ata estruturada e vínculo entre decisões e documentação do Opportunity Ledger. | Sheldon | Consolidar HEARTBEAT + GROWTH_OFFICE + MEMORY em ciclo quinzenal, oficializando ata e checklist antes do próximo encontro. | Ata/documento com próximos passos atualizados e próximos donos claros. |

## 3. Backlog operacional vivo (24/03/2026)
| Oportunidade / Cliente | Frente | Owner | Status | Próximo Passo | Dependência / Bloqueio | Sinal de Receita |
| --- | --- | --- | --- | --- | --- | --- |
| Portal Growth Automation (landing + portal Supabase para PJotaHub) | Captura | Sheldon | Briefing e ICP em andamento; stack Supabase + Claude Code + Codex definidos. | Finalizar ICP, confirmar stack com equipe técnica e agendar diagnóstico de 30 min. | Precisa da equipe escolher janelas e confirmar prazo de entrega. | Estimativa R$ 12k–18k (MVP landing e automações). |
| Conversão automatizada (n8n + Claude + LLMs) | Conversão | Sheldon & Closer | Lead em qualificação; checklist ainda em construção, falta protótipo rápido. | Montar checklist, aplicar no lead e gerar protótipo curto para validar ROI. | Falta tempo técnico para protótipo antes da proposta final. | Proposta potencial de R$ 9k–12k por pacote de automações incrementais. |
| Programa de retenção & vibecoding (cliente atual com metas de engajamento) | Expansão | Sheldon / Builder | Outcome review conduzido, upgrades mapeados e em validação com o cliente. | Roda de valor (40 min) + sugerir retainer de R$ 8k. | Depende da agenda do cliente e da capacidade do Builder. | Retainer mensal de R$ 8k + possíveis upsells. |
| Growth Office Operating Review (estrutura do escritório) | Estratégia interna | Sheldon | Revisão em andamento; gaps estruturais identificados e documentados; GROWTH + HEARTBEAT + MEMORY precisam de sincronização. | Traduzir lacunas em ações (log, checklist, handoff, memória) e agendar o próximo heartbeat com ata. | Precisa de input do Closer e Builder para ordenar backlog vivo e confirmar prioridade. | Cockpit operacional maduro liberando próximos passos claros. |
| Opportunity Ledger (board de captura + CRM leve) | Captura | Sheldon | Sem log central; leads continuam em notas soltas, pipeline perde ritmo. | Modelar board leve (Notion/Airtable/planilha) com origem, ICP, valor, urgência e próximo passo; migrar as oportunidades atuais. | Precisa decidir ferramenta e definir frequência de atualização. | Pipeline com origem, urgência e status visíveis para acelerar follow-up. |
| Ritmo do Growth Office & Memória viva | Estratégia interna | Sheldon | Ritmo quinzenal definido, mas execuções nem sempre registradas; memória vive fora do cockpit. | Amarrar HEARTBEAT + GROWTH_OFFICE + MEMORY em checklist pré-revisão e definir guardião de ata para cada ciclo. | Depende da confirmação do Closer e Builder na cadência quinzenal. | Revisões com ata, backlog atualizado e decisões registradas na memória. |

## 3.1 Opportunity Ledger board
- O board oficial de captura agora vive em OPPORTUNITY_LEDGER.md; ele replica a Seção 3 com colunas extras de origem, ICP, urgência e bloqueios em um template reutilizável.  
- Atualize o arquivo sempre que um item da Seção 3 muda (status, próximos passos ou dependências). Cada HEARTBEAT deve começar consultando o ledger para ver o próximo toque e terminar com ata linkando as linhas tocadas.

## 4. SOPs & Templates (evolução contínua)
### 4.1. Demand routing SOP (revisto)
1. Registrar cada oportunidade nova na tabela da Seção 3 com campo de frente, owner, status e valor esperado.  
2. Incluir sempre origem, ICP e próximo passo com prazo curto (48h/72h) para não deixar o item dormir.  
3. Referenciar riscos, dependências ou decisões na mesma linha para dar contexto ao HEARTBEAT.  
4. Atualizar HEARTBEAT.md antes de cada revisão para garantir alinhamento com o cockpit.  

### 4.2. Checklist captura → conversão
1. Confirmar ICP, impacto e urgência (documentado na Seção 3 ou log paralelo).  
2. Validar decisor(es) e critérios de sucesso (quanto, quando, quem).  
3. Registrar investimento previsto e ROI mínimo esperado.  
4. Criar proposta mínima viável (landing, automação ou portal) e submeter ao Closer com checklist assinado.  
5. Documentar bloqueios, next steps e data de follow-up; só liberar para entrega com sinal verde.  

### 4.3. Handoff para Builder & Ops
- Resumo cliente + proposta + métricas de sucesso.  
- Critérios de sucesso (KPI, prazo, escopo) e checkpoints semanais.  
- Riscos, dependências e plano de mitigação.  
- Canal de comunicação definido (Slack/Notion), frequência de atualização e responsável pela próxima revisão.  
- Status da entrega também aparece neste documento para alimentar transparência.  

### 4.4. Memória viva & HEARTBEAT integration
- Toda decisão relevante ganha linha em MEMORY.md (data + referência ao bloco do documento).  
- Antes da HEARTBEAT, revisar MEMORY.md e conectar entradas ao backlog atual.  
- Difundir aprendizados de cada sprint para que o próximo heartbeat já nasça com contexto.  

### 4.5. Ritmo operacional do Growth Office
1. O ciclo semanal começa revisando as linhas da Seção 3 para verificar quem precisa de movimento.  
2. O heartbeat quinzenal sintetiza esses movimentos em uma ata (quem, o que, quando).  
3. Cada frente (captura, conversão, entrega, expansão e estratégia interna) tem um responsável e um prefeito de próximo passo.  
4. Quando um item muda de status, atualize Seções 2 e 3 simultaneamente para evitar ruído.  

### 4.6. Decision log básico
- Registrar em três colunas (data, decisão, owner) cada vez que o cockpit muda de rumo.  
- Linkar decisions no GROWTH_OFFICE e no MEMORY mesmo que sejam pequenos ajustes de priorização.  

### 4.7. Opportunity ledger & backlog higiene
- O ledger oficial agora mora em OPPORTUNITY_LEDGER.md; use a tabela como origem da verdade e sincronize o status, data do último toque e próximos responsáveis com a Seção 3.  
- Manter colunas mínimas (origem, frente, ICP, valor, urgência, próximo passo, owner, dependências e bloqueios) para cada oportunidade do board.  
- Atualizar o ledger antes de cada HEARTBEAT, marcando o próximo toque, o status atual e o impacto esperado.  
- Garantir que o ledger registre tags de prioridade (MVP/FASE 2/Distração) e evidências concretas de receita ou entrega.  
- Definir guardião da glicose (Sheldon) para verificar se o board está sendo usado e que os líderes atualizam com decisões, bloqueios e mudanças de status.  

### 4.8. Ritual memória + HEARTBEAT
1. Dois dias antes do HEARTBEAT: revisar OPPORTUNITY_LEDGER.md, identificar itens com próximo toque e antecipar riscos pendentes com Closer e Builder.  
2. No dia do checklist: rodar as perguntas do HEARTBEAT, atualizar Seções 2 e 3 e anotar decisões críticas no Decision Log (Seção 4.6).  
3. Após o heartbeat: registrar entrada em MEMORY.md (data, síntese, owner, links) e anexar um resumo rápido ao HEARTBEAT.md para garantir traceability.  
4. Cada mudança de status ou prioridade deve atualizar simultaneamente o ledger, o GROWTH_OFFICE e a ata quinzenal para evitar ruído de memória.

## 5. Memória e estrutura viva
- O Growth Office agora documenta backlog, SOPs e riscos dentro deste arquivo, e o MEMORY.md acompanha com entradas datadas.  
- O backlog da Seção 3 já inclui Opportunity Ledger e Growth Rhythm; atualizar o HEARTBEAT deve trazer links diretos para cada linha e o MEMORY precisa registrar o guardião da ata.  
- HEARTBEAT continua sendo o checklist leve que conecta status atual a decisões e riscos.  
- Antes de cada revisão, alinhar GROWTH_OFFICE + HEARTBEAT + MEMORY e assegurar que cada oportunidade tem owner, próxima ação e dependências claras.  

## 6. Pacotes de trabalho (MVP vs Fase 2)
1. **MVP**: Atualizar a Seção 3 (incluindo Opportunity Ledger e Growth Rhythm), aplicar o checklist capture→conversion no lead mais quente e garantir que o board esteja visível ao Closer. *(Owner: Sheldon, prazo: 25/03/2026; condição: board de oportunidades criado e checklist aplicado).*  
2. **Fase 2**: Estruturar o playbook Builder (handoff + cadência de entrega) e documentar o sprint de valor pós-entrega, alimentando o HEARTBEAT com checkpoints semanais. *(Owner: Sheldon + Builder, prazo: 30/03/2026).*  
3. **Fase 3**: Embutir o ritual de HEARTBEAT + MEMORY + GROWTH, com ata quinzenal, guardião da cadência e integração automática do ledger. *(Owner: Sheldon, prazo: 31/03/2026; condição: cadência quinzenal oficializada).*

## 7. Próximos passos e responsáveis
- **Sheldon**: finalizar briefing do Portal Growth Automation, garantir adoção do Opportunity Ledger (board, template e cadência) com Closer e Builder, aplicar o checklist capture→conversion e garantir que o HEARTBEAT + MEMORY entreguem ata antes da próxima revisão.  
- **Closer**: aplicar checklist de conversão no lead n8n + Claude e registrar validação com Boaventura, entregando evidências até 24/03.  
- **Builder/Ops**: preparar esboço de entrega para o retainer vibecoding, confirmar capacidade para o novo sprint e alimentar os checkpoints do HEARTBEAT até 27/03.  
- **Todos**: revisar HEARTBEAT.md, a Seção 2, o Opportunity Ledger e a seção 3 antes do próximo encontro quinzenal; quem liderar a seção deve registrar ata simples com próximos passos.

## 8. Riscos & decisões estratégicas
- **Risco de pipeline**: a ausência de log central está empurrando oportunidades para notas individuais; sem um board, leads esfriam, e o Closer não consegue priorizar.  
- **Risco de memória e cadência**: sem ata e registro automatizado, decisões e dependências se perdem e o heartbeat vira ruído.  
- **Decisão**: tratar a Seção 3, o Opportunity Ledger, o HEARTBEAT e o MEMORY como a única fonte, atualizando tudo assim que uma linha mudar e garantindo guardião da ata por ciclo.
