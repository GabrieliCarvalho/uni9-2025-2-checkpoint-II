from abc import ABC, abstractmethod

from mensagens import Mensagem  


class ICanal(ABC):
    """
    Define o "contrato" (interface) que todos os canais devem seguir.
    Isso garante que todos terão o método .enviar()
    """
    
    @abstractmethod
    def enviar(self, mensagem: Mensagem, destinatario: str):
        """Método abstrato para enviar uma mensagem."""
        pass



class WhatsApp(ICanal):
    """Implementação do canal WhatsApp."""
    def enviar(self, mensagem: Mensagem, destinatario: str):

        print("---" * 10)
        print(f"CANAL: WhatsApp")
        print(f"DESTINATÁRIO (Telefone): {destinatario}")
        
 
        print(f"MENSAGEM:\n{mensagem.conteudo}") 
        print("---" * 10 + "\n")

class Telegram(ICanal):
    """Implementação do canal Telegram."""
    def enviar(self, mensagem: Mensagem, destinatario: str):

        tipo_dest = "Usuário" if destinatario.startswith("@") else "Telefone"
        
        print("---" * 10)
        print(f"CANAL: Telegram")
        print(f"DESTINATÁRIO ({tipo_dest}): {destinatario}")
        print(f"MENSAGEM:\n{mensagem.conteudo}") 
        print("---" * 10 + "\n")

class Facebook(ICanal):
    """Implementação do canal Facebook."""
    def enviar(self, mensagem: Mensagem, destinatario: str):

        print("---" * 10)
        print(f"CANAL: Facebook")
        print(f"DESTINATÁRIO (Usuário): {destinatario}")
        print(f"MENSAGEM:\n{mensagem.conteudo}") 
        print("---" * 10 + "\n")

class Instagram(ICanal):
    """Implementação do canal Instagram."""
    def enviar(self, mensagem: Mensagem, destinatario: str):

        print("---" * 10)
        print(f"CANAL: Instagram")
        print(f"DESTINATÁRIO (Usuário): {destinatario}")
        print(f"MENSAGEM:\n{mensagem.conteudo}") 
        print("---" * 10 + "\n")