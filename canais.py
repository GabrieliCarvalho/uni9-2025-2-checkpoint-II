from abc import ABC, abstractmethod
from mensagens import Mensagem  


class ICanal(ABC):
 
    
    @abstractmethod
    def enviar(self, mensagem: Mensagem, destinatario: str):
        
        pass



class WhatsApp(ICanal):
    """Implementação do canal WhatsApp."""
    def enviar(self, mensagem: Mensagem, destinatario: str):
        # 'destinatario' é esperado como 'Número de telefone'
        print("---" * 10)
        print(f"CANAL: WhatsApp")
        print(f"DESTINATÁRIO (Telefone): {destinatario}")
        
        # Polimorfismo da Mensagem:
        # Chama .conteudo() sem precisar saber se é MensagemTexto,
        # MensagemVideo ou MensagemFoto.
        print(f"MENSAGEM:\n{mensagem.conteudo}") 
        print("---" * 10 + "\n")

class Telegram(ICanal):
    """Implementação do canal Telegram."""
    def enviar(self, mensagem: Mensagem, destinatario: str):
        # 'destinatario' pode ser 'Número de telefone' ou 'Usuário'
        tipo_dest = "Usuário" if destinatario.startswith("@") else "Telefone"
        
        print("---" * 10)
        print(f"CANAL: Telegram")
        print(f"DESTINATÁRIO ({tipo_dest}): {destinatario}")
        print(f"MENSAGEM:\n{mensagem.conteudo}") # Polimorfismo da Mensagem
        print("---" * 10 + "\n")

class Facebook(ICanal):
    """Implementação do canal Facebook."""
    def enviar(self, mensagem: Mensagem, destinatario: str):
        # 'destinatario' é esperado como 'Usuário'
        print("---" * 10)
        print(f"CANAL: Facebook")
        print(f"DESTINATÁRIO (Usuário): {destinatario}")
        print(f"MENSAGEM:\n{mensagem.conteudo}") # Polimorfismo da Mensagem
        print("---" * 10 + "\n")

class Instagram(ICanal):
    """Implementação do canal Instagram."""
    def enviar(self, mensagem: Mensagem, destinatario: str):
        # 'destinatario' é esperado como 'Usuário'
        print("---" * 10)
        print(f"CANAL: Instagram")
        print(f"DESTINATÁRIO (Usuário): {destinatario}")
        print(f"MENSAGEM:\n{mensagem.conteudo}") # Polimorfismo da Mensagem
        print("---" * 10 + "\n")