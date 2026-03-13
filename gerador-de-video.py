import random

tipos_videos_longos = [
    "Tutorial completo (ex: 'como usar Excel')", "Review detalhado de tecnologia",
    "Vlogs de viagem (Vlog de viagem)", "Vlog de rotina matinal",
    "Entrevista com especialista", "Podcast em vídeo",
    "Gameplay comentada", "Tutorial de montagem de móveis",
    "'React' (reagindo a outros vídeos)", "Vlog de culinária (receita)",
    "Documentário curto", "Vídeo de 'Storytime' (história)",
    "Tour em um local turístico", "Tutorial de Yoga/Exercícios",
    "Resenha de livros (BookTube)", "Dicas de moda e estilo",
    "Experimento científico em casa", "Tour por museum",
    "Vlog de estudo", "Resumo de notícias da semana"
]

tipos_videos_curtos = [
    "Análise de Produto", "Dublagem de áudio viral",
    "Vídeo de dança com transição", "Arrume-se comigo",
    "POV (Point of View) cômico", "Dica rápida de produtividade",
    "Transição de roupa (antes/depois)", "Receita rápida (30 segundos)",
    "'Vida real vs. Instagram'", "Tutorial de maquiagem rápida",
    "Unboxing de produto", "Vídeo motivacional curto",
    "Vlog de um dia de trabalho", "Tour pelo quarto/casa",
    "Desafio de 'faça você mesmo' (DIY)", "Bastidores de um negócio",
    "O que tem na minha bolsa", "Review de filme em 60s",
    "Tutorial de edição de foto", "Reação a um vídeo viral",
    "Mitos e verdades do nicho"
]

tipos_videos_longos_en = [
    "Full tutorial (e.g., 'How to use Excel')", "Detailed tech review",
    "Travel vlogs", "Morning routine vlog", "Interview with an expert",
    "Video podcast", "Commentated gameplay", "Furniture assembly tutorial",
    "'React' video", "Cooking vlog (recipe)", "Short documentary",
    "Storytime video", "Tour of a tourist attraction", "Yoga/Exercise tutorial",
    "Book review (BookTube)", "Fashion and style tips",
    "Home science experiment", "Museum tour", "Study vlog", "Weekly news summary"
]

tipos_videos_curtos_en = [
    "Product analysis", "Viral audio dubbing", "Dance video with transitions",
    "Get ready with me (GRWM)", "Comedic POV (Point of View)",
    "Quick productivity tip", "Outfit transition (before/after)",
    "Quick recipe (30 seconds)", "'Real life vs. Instagram'",
    "Quick makeup tutorial", "Product unboxing", "Short motivational video",
    "Workday vlog", "Room/House tour", "DIY challenge",
    "Business behind-the-scenes", "What's in my bag", "60s movie review",
    "Photo editing tutorial", "Reaction to a viral video", "Niche myths and truths"
]

# --- Lógica do Programa ---

print("Menu Language Selection")
print("01. pt-BR (Português brasileiro)")
print("02. en-US (American English)")

while True:
    language = input("\nSelect the language \n").strip().lower()
    
    # Bloco em Português
    if language in ["01", "1", "pt", "portugues br", "br", "portugues"]:
        while True:
            tipo_curtos = random.choice(tipos_videos_curtos)
            tipo_longos = random.choice(tipos_videos_longos)

            print("\n--- Menu de Ideias ---")
            print("01. Vídeos longos")
            print("02. Vídeos Curtos")
            print("03. Sair")

            respostas = input("Qual ideia você gostaria? \n").strip().lower()

            if respostas in ["01", "1", "vídeos longos", "videos longos"]:
                print("\n✅ Opção sugerida:", tipo_longos)
                exit() 

            elif respostas in ["02", "2", "vídeos curtos"]:
                print("\n✅ Opção sugerida:", tipo_curtos)
                exit()

            elif respostas in ["03", "3", "sair"]:
                print("Saindo...")
                exit()
            else:
                print("\n❌ Opção inválida.")

    # Bloco em Inglês
    elif language in ["02", "2", "en", "english"]:
        while True:
            tipo_curtos_en = random.choice(tipos_videos_curtos_en)
            tipo_longos_en = random.choice(tipos_videos_longos_en)

            print("\n--- Idea Menu ---")
            print("01. Long Videos")
            print("02. Short Videos")
            print("03. Leave")

            respostas = input("What idea would you like? \n").strip().lower()

            if respostas in ["01", "1", "long videos", "long"]:
                print("\n✅ Suggested option:", tipo_longos_en)
                exit()

            elif respostas in ["02", "2", "short videos"]:
                print("\n✅ Suggested option:", tipo_curtos_en)
                exit()

            elif respostas in ["03", "3", "leave"]:
                print("Leaving...")
                exit()
            else:
                print("\n❌ Invalid option.")
    
    # Validação de Erro de Língua
    else:
        print("\n⚠️ Something went wrong! Choose 01 (Português BR) or 02 (American English).")