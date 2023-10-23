import csv

class ColetaDados:
    def __init__(self):
        self.coletados = {'dados': []}
        self.arquivo_csv = 'src/coletadds.csv'
        self.arquivo_csv_cabecalho = ['angle', 'x', 'y']
        self.arquivo_csv_aberto = None
        self.tempo_entre_salva = 60  # Defina o intervalo de tempo desejado em frames (60 frames = 1 segundo)
        self.frames_desde_ultima_salva = 0

    def abrir_arquivo_csv(self):
        if self.arquivo_csv_aberto is None:
            # Crie o arquivo CSV se ele não existir e escreva o cabeçalho
            try:
                self.arquivo_csv_aberto = open(self.arquivo_csv, 'a', newline='')
                writer = csv.DictWriter(self.arquivo_csv_aberto, fieldnames=self.arquivo_csv_cabecalho)
                if self.arquivo_csv_aberto.tell() == 0:
                    writer.writeheader()
            except FileNotFoundError:
                print(f"Não foi possível abrir o arquivo {self.arquivo_csv}")

    def fechar_arquivo_csv(self):
        if self.arquivo_csv_aberto is not None:
            self.arquivo_csv_aberto.close()
            self.arquivo_csv_aberto = None

    def coletar_dados(self, pos_x, pos_y, ang):
        self.abrir_arquivo_csv()
        pos_bola = {'angle': ang, 'x': pos_x, 'y': pos_y}
        self.coletados['dados'].append(pos_bola)
        self.frames_desde_ultima_salva += 1

        if self.frames_desde_ultima_salva >= self.tempo_entre_salva:
            self.salva_dados()
            self.frames_desde_ultima_salva = 0

    def salva_dados(self):
        if self.arquivo_csv_aberto is not None:
            writer = csv.DictWriter(self.arquivo_csv_aberto, fieldnames=self.arquivo_csv_cabecalho)
            for data in self.coletados['dados']:
                writer.writerow(data)
            self.coletados['dados'] = []  # Limpa os dados após a salvamento
        self.fechar_arquivo_csv()
