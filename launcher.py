"""
Editor de Vídeo — O Globo
Launcher para Windows (.exe)
"""
import http.server
import socketserver
import webbrowser
import os
import sys
import mimetypes
import time
import threading

PORT = 8765
HTML = "editor-video-globo.html"

mimetypes.add_type("application/wasm",       ".wasm")
mimetypes.add_type("application/javascript", ".js")
mimetypes.add_type("font/ttf",               ".ttf")


def get_assets_dir():
    """Retorna o diretório de assets, seja em desenvolvimento ou empacotado."""
    if getattr(sys, 'frozen', False):
        # Rodando como .exe (PyInstaller)
        return os.path.join(sys._MEIPASS, 'assets')
    else:
        # Rodando como .py normal
        return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets')


class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cross-Origin-Opener-Policy",   "same-origin")
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        self.send_header("Cache-Control",                "no-store")
        super().end_headers()

    def log_message(self, *args):
        pass  # sem output no console


def abrir_browser():
    time.sleep(1.5)
    url = f"http://localhost:{PORT}/{HTML}"
    for browser_name in ["chrome", "chromium", "msedge"]:
        try:
            b = webbrowser.get(browser_name)
            b.open(url)
            return
        except Exception:
            pass
    webbrowser.open(url)


def main():
    assets = get_assets_dir()
    os.chdir(assets)

    socketserver.TCPServer.allow_reuse_address = True
    try:
        with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
            threading.Thread(target=abrir_browser, daemon=True).start()
            httpd.serve_forever()
    except OSError:
        # Porta já ocupada — servidor já está rodando, só abre o browser
        webbrowser.open(f"http://localhost:{PORT}/{HTML}")
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
