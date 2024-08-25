import pandas as pd
import datetime as dt
import pyautogui
import time
import threading
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import customtkinter as ctk
import tkinter as tk

# Variável global para armazenar o caminho do arquivo e o DataFrame
caminho_arquivo_global = ""
df_global = pd.DataFrame()

# Funções das contas
def conta_1(wait_time=2):
    print("Conta 1")


# Funções das contas
def conta_0(wait_time=2):
    print("Conta 0")

def conta_2(wait_time=2):
    print("Conta 2")
    time.sleep(10)
    # perfil
    pyautogui.click(1159, 992)
    # Menu
    time.sleep(2)
    pyautogui.click(1179, 94)
    # Configurações
    time.sleep(2)
    pyautogui.click(802, 916)
    # Alterar Conta
    time.sleep(2)
    pyautogui.click(755, 647)
    time.sleep(2)
    pyautogui.scroll(-100)
    # Conta 2
    time.sleep(2)
    pyautogui.click(796, 367)
    time.sleep(10)
    pyautogui.click(1160, 281)
    time.sleep(5)
    pyautogui.click(1070, 335)


def conta_3(wait_time=2):
    print("Conta 3")
    time.sleep(10)
    # perfil
    pyautogui.click(1159, 992)
    # Menu
    time.sleep(2)
    pyautogui.click(1179, 94)
    # Configurações
    time.sleep(2)
    pyautogui.click(802, 916)
    # Alterar Conta
    time.sleep(2)
    pyautogui.click(755, 647)
    time.sleep(2)
    pyautogui.scroll(-100)
    # Conta 3
    time.sleep(2)
    pyautogui.click(850, 450)
    time.sleep(10)
    pyautogui.click(1160, 281)
    time.sleep(5)
    pyautogui.click(1070, 335)

def conta_4(wait_time=2):
    print("Conta 4")
    time.sleep(10)
    # perfil
    pyautogui.click(1159, 992)
    # Menu
    time.sleep(2)
    pyautogui.click(1179, 94)
    # Configurações
    time.sleep(2)
    pyautogui.click(802, 916)
    # Alterar Conta
    time.sleep(2)
    pyautogui.click(755, 647)
    time.sleep(2)
    pyautogui.scroll(-100)
    # Conta 4
    time.sleep(2)
    pyautogui.click(849, 529)
    time.sleep(10)
    pyautogui.click(1160, 281)
    time.sleep(5)
    pyautogui.click(1070, 335)

def conta_5(wait_time=2):
    print("Conta 5")
    time.sleep(10)
    # perfil
    pyautogui.click(1159, 992)
    # Menu
    time.sleep(2)
    pyautogui.click(1179, 94)
    # Configurações
    time.sleep(2)
    pyautogui.click(802, 916)
    # Alterar Conta
    time.sleep(2)
    pyautogui.click(755, 647)
    time.sleep(2)
    pyautogui.scroll(-100)
    # Conta 5
    time.sleep(2)
    pyautogui.click(807, 596)
    time.sleep(10)
    pyautogui.click(1160, 281)
    time.sleep(5)
    pyautogui.click(1070, 335)

def conta_6(wait_time=2):
    print("Conta 6")
    time.sleep(10)
    # perfil
    pyautogui.click(1159, 992)
    # Menu
    time.sleep(2)
    pyautogui.click(1179, 94)
    # Configurações
    time.sleep(2)
    pyautogui.click(802, 916)
    # Alterar Conta
    time.sleep(2)
    pyautogui.click(755, 647)
    time.sleep(2)
    pyautogui.scroll(-100)
    # Conta 6
    time.sleep(2)
    pyautogui.click(804, 665)
    time.sleep(10)
    pyautogui.click(1160, 281)
    time.sleep(5)
    pyautogui.click(1070, 335)



def conta_7(wait_time=2):
    print("Conta 7")
    time.sleep(10)
    # perfil
    pyautogui.click(1159, 992)
    # Menu
    time.sleep(2)
    pyautogui.click(1179, 94)
    # Configurações
    time.sleep(2)
    pyautogui.click(802, 916)
    # Alterar Conta
    time.sleep(2)
    pyautogui.click(755, 647)
    time.sleep(2)
    pyautogui.scroll(-100)
    # Conta 7
    time.sleep(2)
    pyautogui.click(822, 740)
    time.sleep(10)
    pyautogui.click(1160, 281)
    time.sleep(5)
    pyautogui.click(1070, 335)


def conta_8(wait_time=2):
    print("Conta 8")
    time.sleep(10)
    # perfil
    pyautogui.click(1159, 992)
    # Menu
    time.sleep(2)
    pyautogui.click(1179, 94)
    # Configurações
    time.sleep(2)
    pyautogui.click(802, 916)
    # Alterar Conta
    time.sleep(2)
    pyautogui.click(755, 647)
    time.sleep(2)
    pyautogui.scroll(-100)
    # Conta 8
    time.sleep(2)
    pyautogui.click(779, 813)
    time.sleep(10)
    pyautogui.click(1160, 281)
    time.sleep(5)
    pyautogui.click(1070, 335)



def conta_9(wait_time=2):
    print("Conta 9")
    time.sleep(10)
    # perfil
    pyautogui.click(1159, 992)
    # Menu
    time.sleep(2)
    pyautogui.click(1179, 94)
    # Configurações
    time.sleep(2)
    pyautogui.click(802, 916)
    # Alterar Conta
    time.sleep(2)
    pyautogui.click(755, 647)
    time.sleep(2)
    pyautogui.scroll(-100)
    # Conta 9
    time.sleep(2)
    pyautogui.click(782, 963)
    time.sleep(10)
    pyautogui.click(1160, 281)
    time.sleep(5)
    pyautogui.click(1070, 335)


def conta_10(wait_time=2):
    print("Conta 10")
    time.sleep(10)
    # perfil
    pyautogui.click(1159, 992)
    # Menu
    time.sleep(2)
    pyautogui.click(1179, 94)
    # Configurações
    time.sleep(2)
    pyautogui.click(802, 916)
    # Alterar Conta
    time.sleep(2)
    pyautogui.click(755, 647)
    time.sleep(2)
    pyautogui.scroll(-100)
    # Conta 10
    time.sleep(2)
    pyautogui.click(791, 958)
    time.sleep(10)
    pyautogui.click(1160, 281)
    time.sleep(5)
    pyautogui.click(1070, 335)

def postar_video(texto, arquivo):
    print("Iniciando a função postar_video...")
    time.sleep(5)
    pyautogui.click(307, 18)
    time.sleep(5)
    pyautogui.click(741, 370)
    time.sleep(2)
    pyautogui.click(1152, 505)
    time.sleep(2)
    pyautogui.click(547, 859)
    time.sleep(4)
    pyautogui.write('videos')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.write(arquivo)
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.click(652, 19)
    time.sleep(3)
    pyautogui.click(984, 377)
    time.sleep(10)
    # perfil
    pyautogui.click(1159, 992)
    # adicionar
    time.sleep(5)
    pyautogui.click(936, 988)
    # clicar no video
    time.sleep(2)
    pyautogui.click(709, 214)
    # publicar
    time.sleep(2)
    pyautogui.click(1072, 984)
    time.sleep(4)
    pyautogui.click(992, 91)
    # publicar
    time.sleep(4)
    pyautogui.click(1072, 984)
    time.sleep(4)
    pyautogui.click(776, 133)
    # texto
    time.sleep(10)
    pyautogui.write(texto)
    time.sleep(2)
    pyautogui.press('enter')
    # publicar
    time.sleep(2)
    pyautogui.click(1072, 984)

def chamar_funcao_conta(n_conta, texto, arquivo):
    funcao_conta = globals().get(f'conta_{n_conta}')
    if funcao_conta:
        funcao_conta()
    else:
        print(f"Função conta_{n_conta} não encontrada.")
    postar_video(texto, arquivo)  # Passa o arquivo como parâmetro

def processar_arquivo_excel(caminho_arquivo):
    global df_global
    # Lendo o arquivo Excel para um DataFrame usando openpyxl
    df_global = pd.read_excel(caminho_arquivo, engine='openpyxl')

    # Limpar a área de texto
    text_output.delete(1.0, tk.END)

    # Exibir as informações da planilha
    #text_output.insert(tk.END, f"Informações da planilha:\n{df}\n\n")

    # Obter a data e hora atuais (objeto datetime)
    data_hora_atual = dt.datetime.now()

    # Formatando a data e hora para um formato legível
    data_hora_formatada = data_hora_atual.strftime("%Y/%m/%d %H:%M:%S")

    # Exibir a data e hora atuais
    text_output.insert(tk.END, f"Data e Hora Atual: {data_hora_formatada}\n\n")

    # Convertendo a coluna 'hora' para um formato de tempo adequado
    df_global['hora'] = df_global['hora'].apply(lambda x: str(x).zfill(8) if isinstance(x, int) or isinstance(x, float) else x)

    # Criando uma coluna de data e hora a partir das colunas existentes
    df_global['data_hora'] = pd.to_datetime(df_global['data'].astype(str) + ' ' + df_global['hora'].astype(str), errors='coerce')

    # Removendo linhas com erros na conversão para datetime
    df_global = df_global.dropna(subset=['data_hora'])

    # Exibir o DataFrame com a nova coluna 'coincide'
    #text_output.insert(tk.END, f"Data e Hora com Comparação:\n{df}\n\n")

    # Verificando se todas as datas e horas são diferentes da atual
    todas_diferentes = ~(df_global['data_hora'] == data_hora_atual)
    if todas_diferentes.all():  # Verifica se todas as datas e horas no DataFrame são diferentes da data e hora atual
        text_output.insert(tk.END, "Todas as datas e horas no DataFrame são diferentes da data e hora atual.\n\n")
    else:
        text_output.insert(tk.END, "Pelo menos uma data e hora no DataFrame coincide com a data e hora atual.\n\n")

    # Filtrando datas e horas posteriores
    df_filtrado = df_global[df_global['data_hora'] > data_hora_atual]

    # Encontrando a data e hora mais próxima
    if not df_filtrado.empty:
        data_hora_min = df_filtrado['data_hora'].min()
        # Formatando e exibindo a data e hora mais próxima
        data_hora_min_formatada = data_hora_min.strftime("%Y/%m/%d %H:%M:%S")
        text_output.insert(tk.END, f"A próxima automação será: {data_hora_min_formatada}\n\n")
    else:
        text_output.insert(tk.END, "Não há datas e horas posteriores ao momento atual no DataFrame.\n\n")

    # Verificando se alguma data e hora coincide exatamente com a data e hora atual
    coincidencias = df_global['data_hora'].apply(lambda x: x.replace(microsecond=0) == data_hora_atual.replace(microsecond=0))

    # Verificando se alguma data e hora coincide com a data e hora atual e chamando a função postar_video se coincidirem
    if coincidencias.any():
        text_output.insert(tk.END, "A função postar_video será iniciada.\n")

        n_conta = df_global[coincidencias]['n_contas'].values[0]
        texto = df_global[coincidencias]['texto'].values[0]
        arquivo = df_global[coincidencias]['arquivo'].values[0]  # Obtém o valor da coluna 'arquivo'

        threading.Thread(target=lambda: chamar_funcao_conta(n_conta, texto, arquivo)).start()
    else:
        text_output.insert(tk.END, "Nenhuma data e hora coincide com a data e hora atual.\n")

def atualizar_tela():
    # Atualiza a data e hora atual na interface
    data_hora_atual = dt.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    label_data_hora.config(text=f"Data e Hora Atual: {data_hora_atual}")

    if caminho_arquivo_global:
        processar_arquivo_excel(caminho_arquivo_global)

    root.after(1000, atualizar_tela)  # Agendar a próxima atualização em 1 segundo (1000 milissegundos)

def carregar_arquivo():
    global caminho_arquivo_global
    caminho_arquivo = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    if caminho_arquivo:
        caminho_arquivo_global = caminho_arquivo
        processar_arquivo_excel(caminho_arquivo_global)
        atualizar_tela()  # Iniciar a atualização periódica após carregar o arquivo

# Funções para mudar a cor do botão quando o mouse passa por cima
def on_enter(event):
    event.widget['background'] = '#cc5700'

def on_leave(event):
    event.widget['background'] = '#FF6F00'

# Configuração da janela principal
root = tk.Tk()
root.title("Automação Kwai")
root.geometry("700x400")
root.configure(bg="#FFA726")  # Cor laranja mais clara

# Estilo do botão
btn_style = ttk.Style()
btn_style.configure('TButton', background='#FFA726', foreground='white', font=('Helvetica', 12, 'bold'))

# Botão para carregar arquivo
btn_carregar = tk.Button(root, text="Carregar Arquivo Excel", bg='#FFA726', fg='white', font=('Helvetica', 12, 'bold'), command=carregar_arquivo)
btn_carregar.bind("<Enter>", on_enter)
btn_carregar.bind("<Leave>", on_leave)
btn_carregar.pack(pady=20)

# Área de texto para exibir informações
text_output = tk.Text(root, wrap=tk.WORD, height=15, width=80, bg="#FFCC80", fg="#333333", font=("Helvetica", 12))  # Cor laranja claro
text_output.pack(expand=True, fill='both', padx=20, pady=10)

# Barra de rolagem para a área de texto
scrollbar = ttk.Scrollbar(root, orient="vertical", command=text_output.yview)
scrollbar.pack(side='right', fill='y')
text_output.configure(yscrollcommand=scrollbar.set)

# Label para exibir a data e hora atual
label_data_hora = tk.Label(root, text="", font=("Helvetica", 16), bg="#FFA726", fg="white")
label_data_hora.pack(pady=10)

root.mainloop()