import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import socket
import psutil
import threading

class AnalisadorRedesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Analisador de Rede - Ambiente Virtual")
        self.root.geometry("800x600")
        
        # Criar interface simples
        self.criar_interface()
    
    def criar_interface(self):
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill='both', expand=True)
        
        # Aba 1: Info
        tab1 = ttk.Frame(notebook)
        notebook.add(tab1, text='Informações')
        
        self.texto = scrolledtext.ScrolledText(tab1, width=70, height=20)
        self.texto.pack(pady=10)
        
        btn_info = ttk.Button(tab1, text="Obter Info da Rede", command=self.mostrar_info)
        btn_info.pack(pady=5)
        
        # Aba 2: Scanner
        tab2 = ttk.Frame(notebook)
        notebook.add(tab2, text='Scanner')
        
        lbl_ip = ttk.Label(tab2, text="IP para scan:")
        lbl_ip.pack(pady=5)
        
        self.entry_ip = ttk.Entry(tab2, width=20)
        self.entry_ip.pack()
        self.entry_ip.insert(0, "127.0.0.1")
        
        btn_scan = ttk.Button(tab2, text="Scanear Portas", command=self.scanear_portas)
        btn_scan.pack(pady=10)
        
        self.resultado = scrolledtext.ScrolledText(tab2, width=70, height=15)
        self.resultado.pack(pady=5)
        
        # Status
        self.status = ttk.Label(self.root, text="Pronto", relief='sunken')
        self.status.pack(fill='x', side='bottom')
    
    def mostrar_info(self):
        info = f"""=== INFORMAÇÕES DO SISTEMA ===

Hostname: {socket.gethostname()}
IP Local: {socket.gethostbyname(socket.gethostname())}

=== INTERFACES DE REDE ===
"""
        for interface, addrs in psutil.net_if_addrs().items():
            info += f"\n{interface}:\n"
            for addr in addrs:
                info += f"  {addr.family.name}: {addr.address}\n"
        
        self.texto.delete(1.0, tk.END)
        self.texto.insert(1.0, info)
        self.status.config(text="Informações obtidas")
    
    def scanear_portas(self):
        ip = self.entry_ip.get()
        self.resultado.delete(1.0, tk.END)
        self.resultado.insert(1.0, f"Scaneando {ip}...\n")
        
        def scan():
            abertas = []
            for porta in range(1, 101):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.1)
                if sock.connect_ex((ip, porta)) == 0:
                    abertas.append(porta)
                    self.resultado.insert(tk.END, f"Porta {porta}: ABERTA\n")
                sock.close()
            
            self.resultado.insert(tk.END, f"\nTotal: {len(abertas)} portas abertas")
            self.status.config(text="Scan completo")
        
        threading.Thread(target=scan, daemon=True).start()
        self.status.config(text="Scan em andamento...")

def main():
    root = tk.Tk()
    app = AnalisadorRedesApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()