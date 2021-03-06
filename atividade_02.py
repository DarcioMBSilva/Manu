# -*- coding: utf-8 -*-
"""atividade_02.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x_Ws22zabdfBMQf8nVsx2j6LN2IKPgk4

# Lab02: Ensaio em motores da Aula 2
---

O objetivo deste ensaio é demonstrar a possibilidade de detectar anomalias no
funcionamento de um motor de indução trifásico (MIT), decorrentes de uma não conformidade das
tensões de alimentação do equipamento, através da análise do sinal de corrente de uma das fases do
motor.

---

## Importanto Bibliotecas
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"""## Condição Normal:

### Operando em vazio
"""

file_name = "https://raw.githubusercontent.com/DarcioMBSilva/Manu/main/Dados_Aula_02_vazio_60Hz_N.lvm"
cond_norm_vazio = pd.read_table(file_name, sep="\t", header=22)
cond_norm_vazio = cond_norm_vazio.rename(columns={"X_Value":"tempo"})
cond_norm_vazio = cond_norm_vazio.drop(columns=["Comment"])
cond_norm_vazio = cond_norm_vazio.apply(lambda x: x.str.replace(',','.'))
cond_norm_vazio = cond_norm_vazio.apply(pd.to_numeric)

# ganhos de tensão 
cond_norm_vazio["VA"] = cond_norm_vazio["VA"]*78.71
cond_norm_vazio["VB"] = cond_norm_vazio["VB"]*80.418
cond_norm_vazio["VC"] = cond_norm_vazio["VC"]*80.667

# ganhos de corrente
cond_norm_vazio["IA"] = cond_norm_vazio["IA"]*4.306
cond_norm_vazio["IB"] = cond_norm_vazio["IB"]*4.302
cond_norm_vazio["IC"] = cond_norm_vazio["IC"]*4.291

f1, ax1 = plt.subplots()
ax1.plot(cond_norm_vazio["tempo"], cond_norm_vazio[["VA", "VB", "VC"]])
ax1.legend(["VA", "VB", "VC"], loc = 4)
ax1.grid(True, linestyle="--")
ax1.set_xlim(0, 4/60)
ax1.set_ylabel('Tensão (V)')
ax1.set_xlabel('Tempo (s)')

#plt.savefig("ten_1.pdf", bbox_inches='tight')

# valores rms

va_rms = np.sqrt((cond_norm_vazio["VA"]**2).mean())
vb_rms = np.sqrt((cond_norm_vazio["VB"]**2).mean())
vc_rms = np.sqrt((cond_norm_vazio["VC"]**2).mean())

print(va_rms, vb_rms, vc_rms)

f2, ax2 = plt.subplots()
ax2.plot(cond_norm_vazio["tempo"], cond_norm_vazio[["IA", "IB", "IC"]])
ax2.legend(["IA", "IB", "IC"], loc = 4)
ax2.grid(True, linestyle="--")
ax2.set_ylabel('Corrente (A)')
ax2.set_xlabel('Tempo (s)')
ax2.set_xlim(0, 4/60)

#plt.savefig("cor_1.pdf", bbox_inches='tight')

# valores rms de corrente

ia_rms = np.sqrt((cond_norm_vazio["IA"]**2).mean())
ib_rms = np.sqrt((cond_norm_vazio["IB"]**2).mean())
ic_rms = np.sqrt((cond_norm_vazio["IC"]**2).mean())

print(ia_rms, ib_rms, ic_rms)

"""### Operando em carga"""

file_name = "https://raw.githubusercontent.com/DarcioMBSilva/Manu/main/Dados_Aula_02_carga_58_5Hz_N.lvm"
cond_norm_carga = pd.read_table(file_name, sep="\t", header=22)
cond_norm_carga = cond_norm_carga.rename(columns={"X_Value":"tempo"})
cond_norm_carga = cond_norm_carga.drop(columns=["Comment"])
cond_norm_carga = cond_norm_carga.apply(lambda x: x.str.replace(',','.'))
cond_norm_carga = cond_norm_carga.apply(pd.to_numeric)

# ganhos de tensão 
cond_norm_carga["VA"] = cond_norm_carga["VA"]*78.71
cond_norm_carga["VB"] = cond_norm_carga["VB"]*80.418
cond_norm_carga["VC"] = cond_norm_carga["VC"]*80.667

# ganhos de corrente
cond_norm_carga["IA"] = cond_norm_carga["IA"]*4.306
cond_norm_carga["IB"] = cond_norm_carga["IB"]*4.302
cond_norm_carga["IC"] = cond_norm_carga["IC"]*4.291

f3, ax3 = plt.subplots()
ax3.plot(cond_norm_carga["tempo"], cond_norm_carga[["VA", "VB", "VC"]])
ax3.legend(["VA", "VB", "VC"], loc = 4)
ax3.grid(True, linestyle="--")
ax3.set_ylabel('Tensão (V)')
ax3.set_xlabel('Tempo (s)')
ax3.set_xlim(0, 4/60)

#plt.savefig("ten_2.pdf", bbox_inches='tight')

# valores rms

va_rms = np.sqrt((cond_norm_carga["VA"]**2).mean())
vb_rms = np.sqrt((cond_norm_carga["VB"]**2).mean())
vc_rms = np.sqrt((cond_norm_carga["VC"]**2).mean())

print(va_rms, vb_rms, vc_rms)

f4, ax4 = plt.subplots()
ax4.plot(cond_norm_carga["tempo"], cond_norm_carga[["IA", "IB", "IC"]])
ax4.legend(["IA", "IB", "IC"], loc = 4)
ax4.grid(True, linestyle="--")
ax4.set_ylabel('Corrente (A)')
ax4.set_xlabel('Tempo (s)')
ax4.set_xlim(0, 4/60)

#plt.savefig("cor_2.pdf", bbox_inches='tight')

# valores rms de corrente

ia_rms = np.sqrt((cond_norm_carga["IA"]**2).mean())
ib_rms = np.sqrt((cond_norm_carga["IB"]**2).mean())
ic_rms = np.sqrt((cond_norm_carga["IC"]**2).mean())

print(ia_rms, ib_rms, ic_rms)

"""## Motor com defeito:

### Operando em vazio
"""

file_name = "https://raw.githubusercontent.com/DarcioMBSilva/Manu/main/Dados_Aula_02_vazio_60Hz_D.lvm"
cond_def_vazio = pd.read_table(file_name, sep="\t", header=22)
cond_def_vazio = cond_def_vazio.rename(columns={"X_Value":"tempo"})
cond_def_vazio = cond_def_vazio.drop(columns=["Comment"])
cond_def_vazio = cond_def_vazio.apply(lambda x: x.str.replace(',','.'))
cond_def_vazio = cond_def_vazio.apply(pd.to_numeric)

# ganhos de tensão 
cond_def_vazio["VA"] = cond_def_vazio["VA"]*78.71
cond_def_vazio["VB"] = cond_def_vazio["VB"]*80.418
cond_def_vazio["VC"] = cond_def_vazio["VC"]*80.667

# ganhos de corrente
cond_def_vazio["IA"] = cond_def_vazio["IA"]*4.306
cond_def_vazio["IB"] = cond_def_vazio["IB"]*4.302
cond_def_vazio["IC"] = cond_def_vazio["IC"]*4.291

f5, ax5 = plt.subplots()
ax5.plot(cond_def_vazio["tempo"], cond_def_vazio[["VA", "VB", "VC"]])
ax5.legend(["VA", "VB", "VC"], loc = 4)
ax5.grid(True, linestyle="--")
ax5.set_ylabel('Tensão (V)')
ax5.set_xlabel('Tempo (s)')
ax5.set_xlim(0, 4/60)

#plt.savefig("ten_3.pdf", bbox_inches='tight')

# valores rms

va_rms = np.sqrt((cond_def_vazio["VA"]**2).mean())
vb_rms = np.sqrt((cond_def_vazio["VB"]**2).mean())
vc_rms = np.sqrt((cond_def_vazio["VC"]**2).mean())

print(va_rms, vb_rms, vc_rms)

f6, ax6 = plt.subplots()
ax6.plot(cond_def_vazio["tempo"], cond_def_vazio[["IA", "IB", "IC"]])
ax6.legend(["IA", "IB", "IC"], loc = 4)
ax6.grid(True, linestyle="--")
ax6.set_ylabel('Corrente (A)')
ax6.set_xlabel('Tempo (s)')
ax6.set_xlim(0, 4/60)

#plt.savefig("cor_3.pdf", bbox_inches='tight')

# valores rms

ia_rms = np.sqrt((cond_def_vazio["IA"]**2).mean())
ib_rms = np.sqrt((cond_def_vazio["IB"]**2).mean())
ic_rms = np.sqrt((cond_def_vazio["IC"]**2).mean())

print(ia_rms, ib_rms, ic_rms)

"""### Operando em carga"""

file_name = "https://raw.githubusercontent.com/DarcioMBSilva/Manu/main/Dados_Aula_02_carga_59Hz_D.lvm"
cond_def_carga = pd.read_table(file_name, sep="\t", header=22)
cond_def_carga = cond_def_carga.rename(columns={"X_Value":"tempo"})
cond_def_carga = cond_def_carga.drop(columns=["Comment"])
cond_def_carga = cond_def_carga.apply(lambda x: x.str.replace(',','.'))
cond_def_carga = cond_def_carga.apply(pd.to_numeric)
cond_def_carga[["VA", "VB", "VC"]] = cond_def_carga[["VA", "VB", "VC"]]

# ganhos de tensão 
cond_def_carga["VA"] = cond_def_carga["VA"]*78.71
cond_def_carga["VB"] = cond_def_carga["VB"]*80.418
cond_def_carga["VC"] = cond_def_carga["VC"]*80.667

# ganhos de corrente
cond_def_carga["IA"] = cond_def_carga["IA"]*4.306
cond_def_carga["IB"] = cond_def_carga["IB"]*4.302
cond_def_carga["IC"] = cond_def_carga["IC"]*4.291

f7, ax7 = plt.subplots()
ax7.plot(cond_def_vazio["tempo"], cond_def_carga[["VA", "VB", "VC"]])
ax7.grid(True, linestyle="--")
ax7.legend(["VA", "VB", "VC"], loc = 4)
ax7.set_ylabel('Tensão (V)')
ax7.set_xlabel('Tempo (s)')
ax7.set_xlim(0, 4/60)

#plt.savefig("ten_4.pdf", bbox_inches='tight')

# valores rms

va_rms = np.sqrt((cond_def_carga["VA"]**2).mean())
vb_rms = np.sqrt((cond_def_carga["VB"]**2).mean())
vc_rms = np.sqrt((cond_def_carga["VC"]**2).mean())

print(va_rms, vb_rms, vc_rms)

f8, ax8 = plt.subplots()
ax8.plot(cond_def_carga["tempo"], cond_def_carga[["IA", "IB", "IC"]])
ax8.legend(["IA", "IB", "IC"], loc = 4)
ax8.grid(True, linestyle="--")
ax8.set_ylabel('Corrente (A)')
ax8.set_xlabel('Tempo (s)')
ax8.set_xlim(0, 4/60)

#plt.savefig("cor_4.pdf", bbox_inches='tight')

# valores rms

ia_rms = np.sqrt((cond_def_carga["IA"]**2).mean())
ib_rms = np.sqrt((cond_def_carga["IB"]**2).mean())
ic_rms = np.sqrt((cond_def_carga["IC"]**2).mean())

print(ia_rms, ib_rms, ic_rms)

"""## FFT"""

def to_db(amp_lin):
  amp_db = 20*np.log10(abs(amp_lin))
  return amp_db

# sistema operando em vazio

# obtenção do sample time e do número de amostras da FFT
N = cond_norm_vazio["tempo"].size
ini = cond_norm_vazio["tempo"].iloc[0]
fim = cond_norm_vazio["tempo"].iloc[-1]
Ts = (fim - ini)/N
n = 8192
nn = 4096

# operando em condição normal
yf_a_n = np.fft.fft(cond_norm_vazio["IA"], n)
yf_b_n = np.fft.fft(cond_norm_vazio["IB"], n)
yf_c_n = np.fft.fft(cond_norm_vazio["IC"], n)

yf_a_n = np.abs(yf_a_n[0:nn])/nn
yf_b_n = np.abs(yf_b_n[0:nn])/nn
yf_c_n = np.abs(yf_c_n[0:nn])/nn

# operando com defeito
yf_a_d = np.fft.fft(cond_def_vazio["IA"], n)
yf_b_d = np.fft.fft(cond_def_vazio["IB"], n)
yf_c_d = np.fft.fft(cond_def_vazio["IC"], n)

yf_a_d = np.abs(yf_a_d[0:nn])/nn
yf_b_d = np.abs(yf_b_d[0:nn])/nn
yf_c_d = np.abs(yf_c_d[0:nn])/nn

# obtenção do vetor de frequência
xf = np.fft.fftfreq(n, Ts)
xf = xf[0:nn]
mx = 500
k = np.arange(0, mx, 60)

#plot dos sinais, operando em condição normal e com defeito 
fig, ax = plt.subplots(3, 1, figsize=(12, 18))

ax[0].plot(xf, to_db(yf_a_n), xf, to_db(yf_a_d))
ax[0].grid(True, linestyle="--")
ax[0].set_xticks(k)
ax[0].set_xlim(55, mx)
ax[0].set_title("(a)", y=-0.1825)
ax[0].set_xlabel('Frequência (Hz)')
ax[0].set_ylabel('Amplitude (dB)')
ax[0].legend(["Condição Normal", "Com defeito"])

ax[1].plot(xf, to_db(yf_b_n), xf, to_db(yf_b_d))
ax[1].grid(True, linestyle="--")
ax[1].set_xticks(k)
ax[1].set_title("(b)", y=-0.1825)
ax[1].set_xlim(0, mx)
ax[1].set_xlabel('Frequência (Hz)')
ax[1].set_ylabel('Amplitude (dB)')
ax[1].legend(["Condição Normal", "Com defeito"])

ax[2].plot(xf, to_db(yf_c_n), xf, to_db(yf_c_d))
ax[2].grid(True, linestyle="--")
ax[2].set_xticks(k)
ax[2].set_xlim(0, mx)
ax[2].set_title("(c)", y=-0.1825)
ax[2].set_ylabel('Amplitude (dB)')
ax[2].set_xlabel('Frequência (Hz)')
ax[2].legend(["Condição Normal", "Com defeito"])

plt.savefig("fft_1.pdf", bbox_inches='tight')
#files.download("fft_vazio.pdf")

fig, ax = plt.subplots(2, 1, figsize=(5, 9))

ax[0].plot(xf, to_db(yf_a_n), xf, to_db(yf_b_n), xf, to_db(yf_c_n))
ax[0].grid(True, linestyle="--")
ax[0].set_xticks(k)
ax[0].set_xlim(0, 500)
ax[0].set_title("Condição Normal")
ax[0].set_ylabel('Amplitude [dB]')
ax[0].legend(['IA', 'IB', 'IC'])

ax[1].plot(xf, to_db(yf_a_d), xf, to_db(yf_b_d), xf, to_db(yf_c_d))
ax[1].grid(True, linestyle="--")
ax[1].set_xticks(k)
ax[1].set_xlim(0, 500)
ax[1].set_title("Com defeito")
ax[1].set_ylabel('Amplitude [dB]')
ax[1].legend(['IA', 'IB', 'IC'])
ax[1].set_xlabel('Frequência [Hz]')

# sistema operando em carga

# obtenção do sample time e do número de amostras da FFT
N = cond_norm_carga["tempo"].size
ini = cond_norm_carga["tempo"].iloc[0]
fim = cond_norm_carga["tempo"].iloc[-1]
Ts = (fim - ini)/N
n = 8192
nn = 4096

# operando em condição normal
yf_a_n = np.fft.fft(cond_norm_carga["IA"], n)
yf_b_n = np.fft.fft(cond_norm_carga["IB"], n)
yf_c_n = np.fft.fft(cond_norm_carga["IC"], n)

yf_a_n = np.abs(yf_a_n[0:nn])/nn
yf_b_n = np.abs(yf_b_n[0:nn])/nn
yf_c_n = np.abs(yf_c_n[0:nn])/nn

# operando com defeito
yf_a_d = np.fft.fft(cond_def_carga["IA"], n)
yf_b_d = np.fft.fft(cond_def_carga["IB"], n)
yf_c_d = np.fft.fft(cond_def_carga["IC"], n)

yf_a_d = np.abs(yf_a_d[0:nn])/nn
yf_b_d = np.abs(yf_b_d[0:nn])/nn
yf_c_d = np.abs(yf_c_d[0:nn])/nn

# obtenção do vetor de frequência
xf = np.fft.fftfreq(n, Ts)
xf = xf[0:nn]
k = np.arange(0, 500, 60)

#plot dos sinais, operando em condição normal e com defeito 
fig, ax = plt.subplots(3, 1, figsize=(12, 18))

ax[0].plot(xf, to_db(yf_a_n), xf, to_db(yf_a_d))
ax[0].grid(True, linestyle="--")
ax[0].set_xlim(0, 500)
ax[0].set_xticks(k)
ax[0].set_title("(a)", y=-0.1825)
ax[0].set_ylabel('Amplitude (dB)')
ax[0].set_xlabel('Frequência (Hz)')
ax[0].legend(["Condição Normal", "Com defeito"])

ax[1].plot(xf, to_db(yf_b_n), xf, to_db(yf_b_d))
ax[1].grid(True, linestyle="--")
ax[1].set_xlim(0, 500)
ax[1].set_xticks(k)
ax[1].set_title("(b)", y=-0.1825)
ax[1].set_ylabel('Amplitude (dB)')
ax[1].set_xlabel('Frequência (Hz)')
ax[1].legend(["Condição Normal", "Com defeito"])

ax[2].plot(xf, to_db(yf_c_n), xf, to_db(yf_c_d))
ax[2].grid(True, linestyle="--")
ax[2].set_xlim(0, 500)
ax[2].set_xticks(k)
ax[2].set_title("(c)", y=-0.1825)
ax[2].set_ylabel('Amplitude (dB)')
ax[2].set_xlabel('Frequência (Hz)')
ax[2].legend(["Condição Normal", "Com defeito"])

plt.savefig("fft_2.pdf", bbox_inches='tight')

fig, ax = plt.subplots(2, 1, figsize=(5, 9))

ax[0].plot(xf, to_db(yf_a_n), xf, to_db(yf_b_n), xf, to_db(yf_c_n))
ax[0].grid(True, linestyle="--")
ax[0].set_xticks(k)
ax[0].set_xlim(0, 500)
ax[0].set_title("Condição Normal")
ax[0].set_ylabel('Amplitude [dB]')
ax[0].legend(['IA', 'IB', 'IC'])

ax[1].plot(xf, to_db(yf_a_d), xf, to_db(yf_b_d), xf, to_db(yf_c_d))
ax[1].grid(True, linestyle="--")
ax[1].set_xticks(k)
ax[1].set_xlim(0, 500)
ax[1].set_title("Com defeito")
ax[1].set_ylabel('Amplitude [dB]')
ax[1].legend(['IA', 'IB', 'IC'])
ax[1].set_xlabel('Frequência [Hz]')