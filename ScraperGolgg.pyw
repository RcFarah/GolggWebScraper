import os
import re
import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

dados = {}
jogadores = []
partida_num = ""

def carregar_jogadores():
    global dados, jogadores, partida_num
    url = entry_url.get().strip()

    # Validar URL
    match = re.search(r'/stats/(\d+)/', url)
    if not match:
        messagebox.showerror("Erro", "Número da partida não encontrado na URL.")
        return
    partida_num = match.group(1)

    # Selenium Setup
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    try:
        tabela = driver.find_element(By.CSS_SELECTOR, "table.completestats")
    except:
        messagebox.showerror("Erro", "Tabela de estatísticas não encontrada.")
        driver.quit()
        return

    linhas = tabela.find_elements(By.TAG_NAME, "tr")
    dados = {}
    num_jogadores = 10

    for linha in linhas:
        cols = linha.find_elements(By.TAG_NAME, "td")
        if len(cols) >= num_jogadores + 1:
            nome_metrica = cols[0].text.strip()
            dados_metrica = [col.text.strip() for col in cols[1:11]]
            dados[nome_metrica] = dados_metrica

    driver.quit()
    jogadores = dados.get("Player", [])

    if not jogadores or all(j == '' for j in jogadores):
        messagebox.showerror("Erro", "Nenhum jogador encontrado.")
        return

    # Atualizar a listbox
    listbox_jogadores.delete(0, tk.END)
    for j in jogadores:
        listbox_jogadores.insert(tk.END, j)

def salvar_dados_selecionados():
    selecao = listbox_jogadores.curselection()
    if not selecao:
        messagebox.showwarning("Aviso", "Nenhum jogador selecionado.")
        return

    metr_sel = [
        "Player", "Role", "Level", "Kills", "Deaths", "Assists", "Solo kills", "KP%",
        "Total damage to Champion", "DPM", "Golds", "GD@15", "LVLD@15", "CSD@15", "CSM", "CS"
    ]

    for idx in selecao:
        jogador = jogadores[idx]
        linhas_texto = []
        for metrica in metr_sel:
            valor = dados.get(metrica, ["N/A"] * len(jogadores))[idx]
            linhas_texto.append(f"{metrica}: {valor}")

        texto_final = f"Dados do jogador '{jogador}' na partida {partida_num}:\n\n" + "\n".join(linhas_texto)

        caminho_base = os.path.join("Jogos", partida_num, jogador)
        os.makedirs(caminho_base, exist_ok=True)

        caminho_arquivo = os.path.join(caminho_base, f"{jogador}_dados.txt")
        with open(caminho_arquivo, "w", encoding="utf-8") as f:
            f.write(texto_final)

    messagebox.showinfo("Sucesso", f"Dados salvos para os jogadores selecionados!")

# --------- Tkinter Interface ---------
janela = tk.Tk()
janela.title("Scraper gol.gg - Estatísticas dos Jogadores")

tk.Label(janela, text="Link da Partida:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry_url = tk.Entry(janela, width=60)
entry_url.grid(row=0, column=1, padx=10, pady=10)

btn_carregar = tk.Button(janela, text="Carregar Jogadores", command=carregar_jogadores)
btn_carregar.grid(row=0, column=2, padx=10)

tk.Label(janela, text="Jogadores disponíveis:").grid(row=1, column=0, padx=10, pady=5, sticky="ne")
listbox_jogadores = tk.Listbox(janela, selectmode=tk.MULTIPLE, width=40, height=10)
listbox_jogadores.grid(row=1, column=1, padx=10, pady=5)

btn_salvar = tk.Button(janela, text="Salvar Dados Selecionados", command=salvar_dados_selecionados, bg="#4CAF50", fg="white")
btn_salvar.grid(row=2, column=0, columnspan=3, pady=20)

janela.mainloop()
