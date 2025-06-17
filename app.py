import os
import sys
import json # Garante que 'json' está importado no topo

# Adicionado 'QStandardPaths' para lidar com caminhos de dados do aplicativo
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QListWidgetItem
from PyQt5.QtCore import QTimer, QTime, Qt, QStandardPaths # QStandardPaths adicionado aqui
from PyQt5.QtGui import QIcon

from ui_main_window import Ui_MainWindow # Importa a classe da interface gerada

class PomodoroApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configura a UI a partir do arquivo gerado pelo Qt Designer
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Define o título da janela (se não definido no Qt Designer)
        self.setWindowTitle("Gerenciador Pomodoro")

        # --- CÓDIGO MELHORADO PARA DEFINIR O ÍCONE DA JANELA ---
        if getattr(sys, 'frozen', False):
            # Se o aplicativo está empacotado (frozen=True)
            application_path = os.path.dirname(sys.path[0]) # sys.path[0] é mais confiável em --onefile
        else:
            # Se o aplicativo está sendo rodado como script Python
            application_path = os.path.dirname(os.path.abspath(__file__))

        # Constrói o caminho completo para o ícone
        icon_path = os.path.join(application_path, "assets", "pomodoro_icon.png")
        
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
            # print(f"Ícone definido de: {icon_path}") # Linha de debug, pode remover depois
        # else:
            # print(f"AVISO: Arquivo de ícone NÃO encontrado em: {icon_path}") # Linha de debug, pode remover depois
        # -------------------------------------------------------------------

        # --- Configurações do Pomodoro ---
        self.pomodoro_duration = 25 * 60 # 25 minutos em segundos
        self.short_break_duration = 5 * 60 # 5 minutos em segundos
        self.long_break_duration = 15 * 60 # 15 minutos em segundos
        self.current_time = self.pomodoro_duration
        self.is_running = False
        self.is_pomodoro = True # True para Pomodoro, False para Pausa
        self.pomodoro_count = 0 # Conta os ciclos de Pomodoro concluídos

        # --- Configuração do QTimer ---
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.update_timer_display() # Atualiza o display inicial

        # --- Conexão dos Botões do Timer ---
        self.ui.btn_start_pause.clicked.connect(self.toggle_timer)
        self.ui.btn_reset.clicked.connect(self.reset_timer)
        self.ui.btn_skip.clicked.connect(self.skip_phase)

        # --- Conexão dos Botões de Tarefas ---
        self.ui.btn_add_task.clicked.connect(self.add_task)
        self.ui.btn_complete_task.clicked.connect(self.complete_task)
        self.ui.btn_remove_task.clicked.connect(self.remove_task)

        # --- Lógica de Salvamento e Carregamento de Dados ---
        self.load_tasks()


    # --- Função auxiliar para obter o caminho de dados ---
    def get_data_path(self):
        """
        Retorna o caminho completo para o arquivo tasks.json
        na pasta de dados do aplicativo (AppData/Roaming no Windows).
        """
        # Obter o caminho padrão para dados de aplicativo específicos do usuário
        # Ex: C:\Users\<Username>\AppData\Roaming\<AppName>
        app_data_root = QStandardPaths.writableLocation(QStandardPaths.AppDataLocation)

        # Criar uma subpasta específica para o seu aplicativo, se não existir
        app_name_folder = "Gerenciador Pomodoro" # Nome da pasta para seus dados
        full_data_dir = os.path.join(app_data_root, app_name_folder)

        # Criar o diretório completo se ele não existir
        os.makedirs(full_data_dir, exist_ok=True) # 'exist_ok=True' evita erro se a pasta já existe

        # Retornar o caminho completo para o arquivo tasks.json
        return os.path.join(full_data_dir, "tasks.json")


    # --- Funções do Timer (métodos) ---
    def update_timer_display(self):
        """Atualiza o QLabel do timer com o tempo formatado."""
        minutes = self.current_time // 60
        seconds = self.current_time % 60
        time_str = f"{minutes:02d}:{seconds:02d}"
        self.ui.lbl_timer.setText(time_str)

    def toggle_timer(self):
        """Inicia/Pausa o timer."""
        if self.is_running:
            self.timer.stop()
            self.ui.btn_start_pause.setText("Iniciar")
        else:
            self.timer.start(1000) # Inicia o timer para disparar a cada 1000ms (1 segundo)
            self.ui.btn_start_pause.setText("Pausar")
        self.is_running = not self.is_running

    def update_timer(self):
        """Decrementa o tempo e lida com o fim de cada fase."""
        if self.current_time > 0:
            self.current_time -= 1
            self.update_timer_display()
        else:
            self.timer.stop()
            self.is_running = False
            self.ui.btn_start_pause.setText("Iniciar")
            self.play_sound_notification()

            if self.is_pomodoro:
                self.pomodoro_count += 1
                if self.pomodoro_count % 4 == 0:
                    QMessageBox.information(self, "Pomodoro Concluído", "Hora da Pausa Longa!")
                    self.current_time = self.long_break_duration
                    self.is_pomodoro = False
                    self.ui.lbl_timer.setStyleSheet("color: blue;") # Muda a cor para indicar pausa longa
                else:
                    QMessageBox.information(self, "Pomodoro Concluído", "Hora da Pausa Curta!")
                    self.current_time = self.short_break_duration
                    self.is_pomodoro = False
                    self.ui.lbl_timer.setStyleSheet("color: green;") # Muda a cor para indicar pausa curta
            else:
                QMessageBox.information(self, "Pausa Concluída", "Hora de voltar ao trabalho!")
                self.current_time = self.pomodoro_duration
                self.is_pomodoro = True
                self.ui.lbl_timer.setStyleSheet("") # Remove estilo (volta ao padrão)
            self.update_timer_display()


    def reset_timer(self):
        """Reseta o timer para a fase atual (Pomodoro ou Pausa)."""
        self.timer.stop()
        self.is_running = False
        self.ui.btn_start_pause.setText("Iniciar")
        if self.is_pomodoro:
            self.current_time = self.pomodoro_duration
        else:
            # Se for pausa, reseta para a duração da pausa atual
            if self.pomodoro_count % 4 == 0: # Se fosse para uma pausa longa
                 self.current_time = self.long_break_duration
            else:
                self.current_time = self.short_break_duration
        self.update_timer_display()
        self.ui.lbl_timer.setStyleSheet("") # Remove qualquer estilo de cor

    def skip_phase(self):
        """Pula a fase atual (Pomodoro para Pausa, Pausa para Pomodoro)."""
        self.timer.stop()
        self.is_running = False
        self.ui.btn_start_pause.setText("Iniciar")
        self.current_time = 1 # Para forçar a transição imediata ao próximo update
        self.update_timer() # Chama para processar o fim da fase atual

    def play_sound_notification(self):
        """Toca um som para notificar o fim de uma fase."""

        print("Som de notificação!")


    # --- Funções de Gerenciamento de Tarefas (métodos) ---
    def add_task(self):
        """Adiciona uma nova tarefa à lista."""
        task_text = self.ui.txt_new_task.text().strip()
        if task_text:
            item = QListWidgetItem(task_text)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setCheckState(Qt.Unchecked)
            self.ui.list_tasks.addItem(item)
            self.ui.txt_new_task.clear() # Limpa o campo de entrada
            self.save_tasks() # Salva as tarefas após adicionar

    def complete_task(self):
        """Marca a tarefa selecionada como concluída (visual)."""
        selected_items = self.ui.list_tasks.selectedItems()
        if selected_items:
            for item in selected_items:
                # Alterna o estado de marcação
                if item.flags() & Qt.ItemIsUserCheckable:
                     if item.checkState() == Qt.Unchecked:
                        item.setCheckState(Qt.Checked)
                     else:
                        item.setCheckState(Qt.Unchecked)
                else:
                    # Se não for checável, adiciona como checável e marca
                    item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
                    item.setCheckState(Qt.Checked)
            self.save_tasks() # Salva o estado das tarefas

    def remove_task(self):
        """Remove a tarefa selecionada da lista."""
        selected_row = self.ui.list_tasks.currentRow()
        if selected_row >= 0:
            self.ui.list_tasks.takeItem(selected_row)
            self.save_tasks() # Salva as tarefas após remover

    # --- Lógica de Persistência de Dados (Salvamento/Carregamento) ---
    def save_tasks(self):
        """Salva as tarefas e seus estados em um arquivo JSON."""
        tasks = []
        for i in range(self.ui.list_tasks.count()):
            item = self.ui.list_tasks.item(i)
            tasks.append({
                "text": item.text(),
                "completed": item.checkState() == Qt.Checked
            })

        file_path = self.get_data_path() # Obtém o caminho correto
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(tasks, f, indent=4)
            print(f"Tarefas salvas em: {file_path}") # Mensagem de debug no console
        except Exception as e:
            # Mostra uma mensagem de erro crítica para o usuário
            QMessageBox.critical(self, "Erro de Salvamento", f"Não foi possível salvar as tarefas:\n{e}\nVerifique permissões ou espaço em disco.")
            print(f"ERRO ao salvar tarefas em {file_path}: {e}") # Mensagem de debug no console


    def load_tasks(self):
        """Carrega as tarefas de um arquivo JSON."""
        file_path = self.get_data_path() # Obtém o caminho correto
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                tasks = json.load(f)
            for task_data in tasks:
                item = QListWidgetItem(task_data["text"])
                item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
                if task_data["completed"]:
                    item.setCheckState(Qt.Checked)
                else:
                    item.setCheckState(Qt.Unchecked)
                self.ui.list_tasks.addItem(item)
            print(f"Tarefas carregadas de: {file_path}") # Mensagem de debug no console
        except FileNotFoundError:
            print("Arquivo tasks.json não encontrado. Iniciando com lista vazia.")
            # Este é um erro esperado na primeira vez que o app é executado
        except json.JSONDecodeError as e:
            QMessageBox.warning(self, "Aviso de Dados", f"O arquivo de tarefas está corrompido e não pôde ser carregado. Erro: {e}")
            print(f"ERRO ao decodificar tasks.json: {e}. Arquivo pode estar corrompido.")
        except Exception as e: # Captura outros erros inesperados ao carregar
            QMessageBox.critical(self, "Erro de Carregamento", f"Ocorreu um erro inesperado ao carregar as tarefas:\n{e}")
            print(f"ERRO inesperado ao carregar tarefas: {e}")


# --- Bloco Principal de Execução ---
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PomodoroApp()
    window.show()
    sys.exit(app.exec_())