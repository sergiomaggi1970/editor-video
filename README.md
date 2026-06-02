# Editor de Vídeo — O Globo

App para aplicar antetítulo, título e marca d'água em vídeos de redes sociais.

## Para usuários finais

Baixe o `Editor-Video-OGlobo.exe` na aba **Releases** (coluna da direita) e dê duplo clique.
Não precisa instalar nada.

## Para gerar um novo .exe (redação)

1. Faça as alterações no `assets/editor-video-globo.html`
2. Commit + Push para o branch `main`
3. O GitHub Actions compila automaticamente em ~3 minutos
4. Baixe o `.exe` novo em **Releases**

## Estrutura

```
launcher.py              ← script principal (compilado no .exe)
editor_globo.spec        ← configuração do PyInstaller
assets/
  editor-video-globo.html
  ffmpeg-core.js
  ffmpeg-core.wasm       ← motor FFmpeg (24 MB)
  ffmpeg-core.worker.js
  ffmpeg.min.js
  046d0074eee1d99a674a.js
  globo-bold.ttf
.github/workflows/
  build.yml              ← pipeline de build automático
```
