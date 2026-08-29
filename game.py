import pygame
import sys

# Pygameの初期化
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Windows Command Prompt (Simulation)")

# カラー設定
BG_COLOR = (12, 12, 12)       # コマンドプロンプトの黒
TEXT_COLOR = (204, 204, 204)  # 通常の白文字
SUCCESS_COLOR = (0, 255, 102) # ハック成功時の緑
ERROR_COLOR = (255, 51, 51)   # エラー文字（ホラー風演出用）

# フォント設定（日本語対応のMSゴシックに固定）
FONT_SIZE = 16
font = pygame.font.SysFont("msgothic", FONT_SIZE)

# 起動メッセージ（Windows風）
lines = [
    "Microsoft Windows [Version 10.0.26300.9032]",
    "(c) Microsoft Corporation. All rights reserved.",
    ""
]
current_input = ""

# ゲームの環境変数（初期状態のPATH）
current_path = "C:\\Windows\\system32;C:\\Windows;C:\\Python314"
game_clear = False
glitch_active = False

def process_command(cmd):
    """入力されたコマンドを判定するゲームのコアロジック"""
    global current_path, game_clear, glitch_active
    cmd_lower = cmd.strip().lower()
    
    if not cmd_lower:
        return [""]
        
    # 1. import import コマンドの判定
    if cmd_lower == "import import":
        if "core" in current_path.lower():
            game_clear = True
            glitch_active = True
            return [
                "[CRITICAL] ACCESS GRANTED.",
                "[SYSTEM] Patching Python vocabulary rules...",
                "[SUCCESS] 'import' successfully imported into 'import'!",
                "==================================================",
                " CONGRATULATIONS: YOU HACKED THE LANGUAGE BARRIER!",
                "==================================================",
                "Press ENTER to shutdown the system..."
            ]
        else:
            return ["'import' は、内部コマンドまたは外部コマンド、",
                    "操作可能なプログラムまたはバッチ ファイルとして認識されていません。"]
                    
    # 2. path コマンド（現在のPATH確認）
    elif cmd_lower == "path":
        return [f"PATH={current_path}"]
        
    # 3. set path=... コマンド（PATHの書き換え）
    elif cmd_lower.startswith("set path="):
        new_path = cmd[9:].strip()
        if not new_path:
            return ["環境変数 PATH がクリアされました。"]
        current_path = new_path
        
        if "core" in new_path.lower():
            return [
                f"PATH={current_path}",
                "[NOTICE] A hidden directory 'core' has been linked to the system PATH."
            ]
        return [f"PATH={current_path}"]
        
    # 4. ヘルプコマンド
    elif cmd_lower == "help":
        return [
            "利用可能なコマンド:",
            "  path       - 現在の環境変数PATHを表示します。",
            "  set path=  - 環境変数PATHを書き換えます。",
            "               (隠されたコアディレクトリにパスを通せ！)"
        ]
        
    # 5. その他の通常コマンド（偽エラー）
    else:
        # 最初の単語を取得
        first_word = cmd.split()[0] if cmd.split() else cmd
        return [f"'{first_word}' は、内部コマンドまたは外部コマンド、",
                "操作可能なプログラムまたはバッチ ファイルとして認識されていません。"]

# メインループ
clock = pygame.time.Clock()
frame_count = 0

while True:
    frame_count += 1
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        elif event.type == pygame.KEYDOWN:
            if game_clear:
                if event.key == pygame.K_RETURN:
                    pygame.quit()
                    sys.exit()
                continue
                
            if event.key == pygame.K_RETURN:
                lines.append(f"C:\\Users\\arks2_dc4cden>{current_input}")
                output_lines = process_command(current_input)
                lines.extend(output_lines)
                lines.append("") # 改行用空行
                current_input = ""
            elif event.key == pygame.K_BACKSPACE:
                current_input = current_input[:-1]
            else:
                if len(current_input) < 60:
                    current_input += event.unicode

    # 画面描画
    screen.fill(BG_COLOR)
    
    # 最新の行だけを表示
    max_visible_lines = (HEIGHT - 50) // (FONT_SIZE + 4)
    display_lines = lines[-max_visible_lines:] if len(lines) > max_visible_lines else lines

    y_offset = 20
    for line in display_lines:
        color = SUCCESS_COLOR if game_clear and ("[SUCCESS]" in line or "CONGRATULATIONS" in line) else TEXT_COLOR
        if "[CRITICAL]" in line or "[SYSTEM]" in line:
            color = ERROR_COLOR
            
        text_surface = font.render(line, True, color)
        screen.blit(text_surface, (20, y_offset))
        y_offset += FONT_SIZE + 4
        
    # 入力行の描画
    if not game_clear:
        prompt = "C:\\Users\\arks2_dc4cden>"
        input_text = f"{prompt}{current_input}"
        input_surface = font.render(input_text, True, TEXT_COLOR)
        screen.blit(input_surface, (20, y_offset))
        
        # 【修正】font.size()[0] で確実に横幅（数値）だけを足し算する
        if (frame_count // 30) % 2 == 0:
            text_width = font.size(input_text)[0]
            cursor_x = 20 + text_width
            pygame.draw.rect(screen, TEXT_COLOR, (cursor_x, y_offset + 2, 10, FONT_SIZE - 2))

    pygame.display.flip()
    clock.tick(60)
