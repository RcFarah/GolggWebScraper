# 📊 Gol.gg Match Scraper

Um scrapper automatizado com interface gráfica para extração de estatísticas detalhadas de jogadores em partidas profissionais de League of Legends, utilizando o site [**gol.gg**](https://gol.gg/). como fonte.

---

## 🚀 Funcionalidades

* **Extração Automatizada:** Utiliza Selenium em modo *headless* para navegar e coletar dados de tabelas complexas.
* **Interface Gráfica (GUI):** Desenvolvida em Tkinter para facilitar o uso sem necessidade de terminal.
* **Seleção Múltipla:** Permite carregar a lista de jogadores da partida e selecionar quais perfis deseja exportar.
* **Exportação Organizada:** Salva os dados em arquivos `.txt` estruturados por número de partida e nome do jogador.
* **Métricas Detalhadas:** Coleta dados como Kills, Deaths, Assists, Solo Kills, DPM, GD@15, CSM, entre outros.

---

## 🛠️ Stack Técnica

* **Linguagem:** Python 3.x.
* **Automação Web:** [Selenium WebDriver](https://www.selenium.dev/).
* **Interface:** Tkinter.
* **Regex:** Processamento de URLs para identificação de partidas.

---

## 📂 Como Executar

### 1. Pré-requisitos
* Python instalado.
* Chrome instalado (o Selenium utilizará o ChromeDriver automaticamente).

### 2. Instalação
Clone o repositório e instale a dependência do Selenium:
```bash
pip install selenium
```
### 3. Execução
Para iniciar a aplicação, execute o script principal:
```bash
python ScrapperGolgg.pyw
```
---

## 📖 Como Usar

1. **Inserir URL**: Copie e cole a URL completa de uma partida do site **gol.gg** (ex: `https://gol.gg/game/stats/XXXXX/page-fullstats/`) no campo indicado (NOTE QUE PRECISA SER DA PÁGINA FULLSTATS).
2. **Carregar Jogadores**: Clique no botão **"Carregar Jogadores"**. O script utilizará o Selenium em modo *headless* para extrair a lista de atletas da partida diretamente da tabela de estatísticas.
3. **Selecionar Perfis**: Na lista que aparecerá no centro da interface, você pode selecionar um ou múltiplos jogadores que deseja analisar.
4. **Exportar Dados**: Clique em **"Salvar Dados Selecionados"**.
5. **Verificar Resultados**: O programa criará automaticamente uma estrutura de pastas no formato `Jogos/[ID_DA_PARTIDA]/[NOME_DO_JOGADOR]` e salvará um arquivo `.txt` contendo métricas como Kills, Deaths, Assists, Solo Kills, DPM, GD@15 e CSM.

---

## 👨‍💻 Autor

**Rodrigo Corrêa de Sá Farah** *Graduando em Ciência da Computação – Universidade Veiga de Almeida (UVA)*

---

## 📜 Licença

Este projeto foi desenvolvido para fins de estudo e automação de coleta de dados para análise de performance em Esports. Sinta-se à vontade para utilizar como referência ou para suas próprias análises.
