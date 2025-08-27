# Planify

Planify é uma aplicação web para organizar tarefas diárias a partir de uma tabela Excel. O usuário faz upload de um arquivo Excel com horários e tarefas, e o sistema transforma cada célula em tarefas organizadas por dia e hora. As tarefas do dia atual são exibidas em formato de checklist, permitindo marcar como concluídas.

## Funcionalidades

- **Upload de Excel:** Envie uma tabela Excel com colunas `day_of_week`, `time`, `description`.
- **Checklist diário:** Veja as tarefas do dia atual, filtradas automaticamente.
- **Marcar como concluída:** Marque/desmarque tarefas e salve o progresso.
- **Histórico de tarefas (opcional):** Consulte tarefas de outros dias.

## Tecnologias

- **Backend:** Django + Django REST Framework
- **Frontend:** React
- **Banco de dados:** SQLite (padrão) ou PostgreSQL
- **Leitura de Excel:** pandas/openpyxl

## Instalação e Execução

1. Clone o repositório e acesse a pasta do projeto.
2. Execute o script de setup:
   ```bash
   chmod +x setup_planify.sh
   ./setup_planify.sh
   ```
3. Acesse [http://localhost:3000](http://localhost:3000) no navegador.

## Como usar

1. Na página inicial, faça upload do arquivo Excel.
2. Veja as tarefas do dia atual em formato de checklist.
3. Marque/desmarque tarefas conforme concluir.
4. As alterações são salvas automaticamente no banco de dados.

## Estrutura do Excel

O arquivo deve conter as colunas:
- `day_of_week` (ex: Monday, Tuesday, ...)
- `time` (ex: 08:00, 14:30, ...)
- `description` (ex: "Reunião", "Estudar", ...)

## Observações

- O backend roda em `localhost:8000` e o frontend em `localhost:3000`.
- Para uso em produção, configure variáveis de ambiente e banco de dados conforme necessário.

---
